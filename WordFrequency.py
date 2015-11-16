#
# WordFrequency.py
#
# defines class WordFrequency and related utility functions
#

import collections
import cmath
import cPickle


class WordFrequency:
    def __init__(self):
        self.dict = collections.defaultdict(int)
        self.total = long(0)

    def add_word_sequence(self, seq):
        for word in seq:
            self.dict[word] += 1
            self.total += 1

    def add_word_freq_pair(self, word, freq):
        self.dict[word] += freq
        self.total += freq

    def total(self):
        return self.total

    def get_frequency(self, word):
        return self.dict[word]

    def get_probability(self, word, missing=None):
        if word in self.dict:
            return float(self.dict[word])/self.total
        elif missing:
            return missing(word)
        else:
            return 1.0 / self.total

    def get_log_probability(self, word):
        return cmath.log10(self.get_probability(word))

    def __contains__(self, item):
        return item in self.dict

    def __len__(self):
        return len(self.dict)

    def __getitem__(self, item):
        return self.get_frequency(item)

    def __iter__(self):
        return iter(self.dict)

    @staticmethod
    def from_freq_file(file_name):
        result = WordFrequency()
        for line in open(file_name, 'r'):
            tokens = line.split()
            word = tokens[0]
            freq = int(tokens[1])
            result.add_word_freq_pair(word, freq)
        return result

    def pickle(self, file_name):
        f = open(file_name, "wb")
        cPickle.dump(self, f)
        f.close()

    @staticmethod
    def unpickle(file_name):
        f = open(file_name, "rb")
        result = cPickle.load(f)
        f.close()
        return result
