from Context import Context
from EditDistance import edits
from WordFrequency import WordFrequency
import re
import Readers

count_1w = WordFrequency.from_freq_file("data/Norvig/wordfreqs/count_1w.txt")
count_2w = WordFrequency.from_freq_file("data/Norvig/wordfreqs/count_2w.txt")



def corrections(text):
    "Spell-correct all words in text."
    return re.sub('[a-zA-Z]+', lambda m: correct(m.group(0)), text)

def correct(context):
    "Return the word that is the most likely spell correction of w."
    candidates = edits(context.word()).items()

    #c, edit = max(candidates, key=lambda (c,e): Pedit(e) * Pw(c))
    #return c


for context in Context.gen_context_sequence_from_word_sequence(Readers.gen_words_from_file("doc.txt")):
    correct(context)