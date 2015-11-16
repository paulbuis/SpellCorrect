from re import findall

# would prefer to segment on sentence boundaries rather than line boundaries
# but having problems with nltk
# from nltk.tokenize import sent_tokenize, word_tokenize


# def gen_sentences_from_file(file_name):
#    f = file(file_name)
#    raw_text = f.read()
#    for sent in sent_tokenize(raw_text):
#        yield sent
#    f.close()


# def gen_words_from_sentence(sent):
#    for word in word_tokenize(sent):
#        yield word


# def gen_words_from_file(file_name):
#    for sent in gen_sentences_from_file(file_name):
#        for word in gen_words_from_sentence(sent):
#            yield word


def gen_words_from_file(file_name):
    f = open(file_name)
    for raw_line in f:
        for word in findall('[a-z]+', raw_line.lower()):
            yield word
    f.close()
