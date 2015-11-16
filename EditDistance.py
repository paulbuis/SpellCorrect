#
# EditDistance.py
#
# functions relating to edit distance
#
from WordFrequency import WordFrequency

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def edits1(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


def datafile(name, sep='\t'):
    """Read key,value pairs from file."""
    for line in file(name):
        yield line.split(sep)


edit_frequencies = WordFrequency.from_freq_file('Norvig/edits/count_1edit.txt')


p_spell_error = 1./20.


def p_edit(edit):
    """The probability of an edit; can be '' or 'a|b' """
    if edit == '':
        return 1. - p_spell_error
    return p_spell_error * edit_frequencies.get_probability(edit)

PREFIXES = set(w[:i] for w in Pw for i in range(len(w) + 1))


def edits(word, dictionary, d=2):
    """Return a dict of {correct: edit} pairs within d edits of word."""
    results = {}

    def edits_recurse(hd, tl, d_recurse, edits):

        def ed(left, right):
            return edits + [right + '|' + left]

        cons = hd+tl
        if cons in dictionary:
            e = '+'.join(edits)
            if cons not in results:
                results[cons] = e
            else:
                results[cons] = max(results[cons], e, key=p_edit)
        if d_recurse <= 0:
            return

        extensions = [hd+c for c in alphabet if hd+c in PREFIXES]
        p = (hd[-1] if hd else '<')  # previous character

        # Insertion
        for h in extensions:
            edits_recurse(h, tl, d_recurse-1, ed(p+h[-1], p))
        if not tl:
            return

        # Deletion
        edits_recurse(hd, tl[1:], d_recurse-1, ed(p, p+tl[0]))
        for h in extensions:
            # noinspection PyPep8
            if h[-1] == tl[0]:  # Match
                edits_recurse(h, tl[1:], d_recurse, edits)
            else:  # Replacement
                edits_recurse(h, tl[1:], d_recurse-1, ed(h[-1], tl[0]))

        # Transpose
        if len(tl) >= 2 and tl[0] != tl[1] and hd+tl[1] in PREFIXES:
            edits_recurse(hd+tl[1], tl[0]+tl[2:], d_recurse-1, ed(tl[1]+tl[0], tl[0:2]))

    # Body of edits:
    edits_recurse('', word, d, [])
    return results
