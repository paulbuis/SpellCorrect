#
# Context.py
#
# defines class Context and related utility functions
#
# Represents a word (or a proposed replacement) from a document with along with its
# context of surrounding words. The context can be evaluated as a probability and
# then the probabilities of all proposed replacements can be compared


def concat_with_space2(t):
    if t is None:
        return None
    assert isinstance(t, tuple)
    a, b = t
    if (not isinstance(a, str)) or (not isinstance(b, str)):
        return ''
    result = a + ' ' + b
    # assert isinstance(result, str)
    return result


def concat_with_space3(t):
    if t is None:
        return None
    assert isinstance(t, tuple)
    a, b, c = t
    if (not isinstance(a, str)) or (not isinstance(b, str)) or (not isinstance(c, str)):
        return ''
    result = a + ' ' + b + ' ' + c
    # assert isinstance(result, str)
    return result


class Context:
    def __init__(self, word, two_gram_pre, two_gram_post, three_gram_centered, three_gram_pre, three_gram_post):
        assert(word is not None)
        assert(isinstance(word, str))
        assert ((two_gram_pre is None) or isinstance(two_gram_pre, tuple))
        assert ((two_gram_post is None) or isinstance(two_gram_post, tuple))
        assert ((three_gram_centered is None) or isinstance(three_gram_centered, tuple))
        assert ((three_gram_pre is None) or isinstance(three_gram_pre, tuple))
        assert ((three_gram_post is None) or isinstance(three_gram_post, tuple))
        self.word = word
        self.two_gram_pre = two_gram_pre
        self.two_gram_post = two_gram_post
        self.three_gram_centered = three_gram_centered
        self.three_gram_pre = three_gram_pre
        self.three_gram_post = three_gram_post

    def two_gram_pre_str(self):
        result = concat_with_space2(self.two_gram_pre)
        if result is None:
            return ''
        return result

    def two_gram_post_str(self):
        if self.two_gram_post is None:
            return ''
        return concat_with_space2(self.two_gram_post)

    def three_gram_centered_str(self):
        if self.three_gram_centered is None:
            return ''
        return concat_with_space3(self.three_gram_centered)

    def three_gram_pre_str(self):
        result = concat_with_space3(self.three_gram_pre)
        if result is None:
            return ''
        return result

    def three_gram_post_str(self):
        result = concat_with_space3(self.three_gram_post)
        if result is None:
            return ''
        return result

    def __str__(self):
        two_pre = self.two_gram_pre_str()
        two_post = self.two_gram_post_str()
        three_centered = self.three_gram_centered_str()
        three_pre = self.three_gram_pre_str()
        three_post = self.three_gram_post_str()
        return self.word + '\r\n' + \
            two_pre + '\r\n' +\
            two_post + '\r\n' +\
            three_centered + '\r\n' +\
            three_pre + '\r\n' +\
            three_post

    def replace_word(self, new_word):
        new2pre = self.two_gram_pre[0], new_word
        new2post = new_word, self.two_gram_post[1]
        new3centered = self.three_gram_centered[0], new_word, self.three_gram_centered[2]
        new3pre = self.three_gram_pre[0], self.three_gram_pre[1], new_word
        new3post = new_word, self.three_gram_post[1], self.three_gram_post[2]
        return Context(new_word, new2pre, new2post, new3centered, new3pre, new3post)

    @staticmethod
    def gen_context_sequence_from_word_sequence(words):
        last4 = None
        last3 = None
        last2 = None
        last1 = None

        for word in words:
            curr_word = word
            two_gram_pre = last3, last2
            two_gram_post = last2, last1
            three_gram_centered = last3, last2, last1
            three_gram_pre = last4, last3, last2
            three_gram_post = last2, last1, curr_word
            if last2 is not None:
                yield Context(last2, two_gram_pre, two_gram_post, three_gram_centered, three_gram_pre, three_gram_post)
            last4 = last3
            last3 = last2
            last2 = last1
            last1 = curr_word

        two_gram_pre = last3, last2
        two_gram_post = last2, last1
        three_gram_centered = last3, last2, last1
        three_gram_pre = last4, last3, last2
        three_gram_post = last2, last1, None
        yield Context(last2, two_gram_pre, two_gram_post, three_gram_centered, three_gram_pre, three_gram_post)

        two_gram_pre = last2, last1
        two_gram_post = last1, None
        three_gram_centered = last2, last1, None
        three_gram_pre = last3, last2, last1
        three_gram_post = last1, None, None
        yield Context(last1, two_gram_pre, two_gram_post, three_gram_centered, three_gram_pre, three_gram_post)
