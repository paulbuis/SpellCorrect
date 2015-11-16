#
# Corpus.py
#
# defines class Corpus and related utility functions
#
from WordFrequency import WordFrequency


class Corpus:
    def __init__(self, words):
        self.one_gram_freq = WordFrequency()
        self.two_gram_freq = WordFrequency()
        self.three_gram_freq = WordFrequency()

        last2_word = None
        last1_word = None
        for curr_word in words:
            self.one_gram_freq[curr_word] += 1
            if last1_word is not None:
                self.two_gram_freq[last1_word + ' ' + curr_word] += 1
            if last2_word is not None:
                self.three_gram_freq[last2_word + ' ' + last1_word + ' ' + curr_word] += 1
            last2_word = last1_word
            last1_word = curr_word

