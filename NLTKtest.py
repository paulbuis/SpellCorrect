# for more information on using NLTK to segment and tokenize, see
# http://nltk.googlecode.com/svn/trunk/doc/howto/tokenize.html
# and chapter 3.8 of the NLTK book:
# http://nltk.googlecode.com/svn/trunk/doc/book/ch03.html#sec-segmentation

import re

import nltk.data
from nltk.tokenize.treebank import TreebankWordTokenizer

sentence_tokenizer = nltk.data.load('data/nltk/punkt/english.pickle')


def sent_tokenize(text):
    """
    Return a sentence-tokenized copy of *text*,
    using NLTK's recommended sentence tokenizer
    (currently :class:`.PunktSentenceTokenizer`).
    """
    return sentence_tokenizer.tokenize(text)


word_tokenizer = TreebankWordTokenizer().tokenize


def word_tokenize(sent):
    """
    Return a tokenized copy of *text*, assuming *text* is a single sentence
    using NLTK's recommended word tokenizer
    (currently :class:`.TreebankWordTokenizer`

    Modifited  so it discards tokens that are purely non-word characters
    """
    return [token for token in word_tokenizer(sent) if re.match('\w+', token)]


def gen_sentences_from_file(file_name):
    f = file(file_name)
    raw_text = f.read()
    for sent in sent_tokenize(raw_text):
        yield sent
    f.close()


def gen_words_from_sentence(sent):
    for word in word_tokenize(sent):
        yield word


def gen_words_from_file(file_name):
    for sent in gen_sentences_from_file(file_name):
        yield '<S>'
        for word in gen_words_from_sentence(sent):
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
