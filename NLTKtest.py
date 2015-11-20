# for more information on using NLTK to segment and tokenize, see
# http://nltk.googlecode.com/svn/trunk/doc/howto/tokenize.html
# and chapter 3.8 of the NLTK book:
# http://nltk.googlecode.com/svn/trunk/doc/book/ch03.html#sec-segmentation
# or just read the source, the parts we are using don't seem particularly difficult

# for use with this project, this code should be integrated into Readers.py
# here we are just playing with NLTK to see how it works

# this file can be omitted from any final code distribution, it should not
# be the object of an import statement elsewhere

import re

import nltk.data
from nltk.tokenize.treebank import TreebankWordTokenizer

sentence_tokenizer = nltk.data.load('data/nltk/punkt/english.pickle')
word_tokenizer = TreebankWordTokenizer().tokenize


def gen_sentences_from_file(file_name):
    f = file(file_name)
    raw_text = f.read()
    for sent in sentence_tokenizer.tokenize(raw_text):
        yield sent
    f.close()


def gen_words_from_file(file_name):
    '''
    :param file_name: name of text document file being analyzed
    :return: sequence of words with pseudo-words <S> inserted at start of sentence and <E> inserted at end of sentence

    pseudo-words important for context-based spell checking. The bigram "<S> The" makes it likely that capitalization of
    the word "The" is preferred of a non-captilized version
    '''
    for sent in gen_sentences_from_file(file_name):
        words = [token for token in word_tokenizer(sent) if re.match('\w+', token)]
        if words:
            yield '<S>'
            for word in words:
                yield word
            yield '<E>'


def test1():
    print '\ntesting gen_sentences_from file'
    for sent in gen_sentences_from_file("doc.txt"):
        print sent


def test2():
    print '\ntesting gen_words_from file'
    for word in gen_words_from_file("doc.txt"):
        print word


test1()
print '\n===================================\n'
test2()
