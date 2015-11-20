Corpus used in Peter Norvig's simplistic spelling corrector found at http://norvig.com/spell-correct.html

Vocabulary size about 14,000 words. To make usable, see techniques in
http://norvig.com/ngrams/ch14.pdf which provide for a non-zero probablility
of words not in a frequency table.

I also suggest considering appending a wordlist of "dictionary" words to
this file to make dictionary words more likely than "words" in neither
a modest corpus (like this one) nor the wordlist. This idea is not discussed
by Norvig, so may not be ideal.
