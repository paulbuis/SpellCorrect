from Readers import Corpus, gen_contexts
#import DocumentReaders.Readers.Context as Context
#import DocumentReaders.Readers.gen_contexts as gen_contexts



# corpus = Corpus("doc.txt")
# for k, v in sorted(corpus.one_gram_freq.items()):
#    print k, v
# for k, v in sorted(corpus.two_gram_freq.items()):
#    print k, v
#  for k, v in sorted(corpus.three_gram_freq.items()):
#    print k, v

for context in gen_contexts("doc.txt"):
    s = str(context)
    print s
    print "================================================"

