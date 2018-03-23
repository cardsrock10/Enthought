"""
Concordance
------------

We would like to be able to search a given text for a word and then print that
word in context everywhere it is found. This is called a "concordance".

NOTE: This exercise uses some default NLTK corpora, which first needs to be
downloaded. In an IPython prompt,
    >>> import nltk
    >>> nltk.download_shell()
Then select download and select the package `gutenberg`. For more details,
please refer to http://www.nltk.org/data.html.

1. Write a function show_word_in_context that takes 2 inputs, a word and a
text, and prints the text around each occurrence of the word (5 words on each
side).

2. Test your function for example on sample texts available in nltk:

    >>> from nltk.corpus import gutenberg
    >>> text = gutenberg.raw('melville-moby_dick.txt')
    >>> show_word_in_context('scared', text)


3. Make your function smarter by using stemming so that derived versions of the
word passed are found as well. Does punctuation affect stemming? Make the
function smarter by removing punctuation.
"""

import nltk
from string import punctuation

text = nltk.corpus.gutenberg.raw('melville-moby_dick.txt')

# 1.Write a function show_word_in_context that takes 2 inputs, a word and a
# text, and prints the text around each occurrence of the word (5 words on each
# side).


def show_word_in_context(target_word, text, context_size=5):
    """ Simplest concordance searching tool. """
    text = text.lower()
    target_word = target_word.lower()

    words = nltk.word_tokenize(text)

    for word_num, word in enumerate(words):
        if word == target_word:
            start = max(word_num - context_size, 0)
            stop = word_num + context_size + 1
            words_around = words[start: stop]
            print " ".join(words_around)


# 2. Test your function for example on sample texts available in nltk:
print "Version 1:"
show_word_in_context("scared", text)

# 3. Make your function smarter by using stemming so that derived versions of
# the word passed are found as well.


def show_word_in_context2(target_word, text, context_size=5):
    """ Better concordance searching tool: stemmer used and punctuation removed
    """
    stemmer = nltk.LancasterStemmer()

    # Target word pre-processing
    target_stem = stemmer.stem(target_word.lower())

    # Text pre-processing
    text = text.lower()
    for punct in punctuation:
        text = text.replace(punct, " ")

    # Make a bag of words, retaining order
    words = nltk.word_tokenize(text)

    # Search and print
    text_parts = []
    for word_num, word in enumerate(words):
        if stemmer.stem(word) == target_stem:
            start = max(word_num - context_size, 0)
            stop = word_num + context_size + 1
            text_parts.append(words[start: stop])

    return text_parts


print "Version 2:"
text_parts = show_word_in_context2("scared", text)
print "Found {} occurences:".format(len(text_parts))
for part in text_parts:
    print " ".join(part)

# Bonus
# ~~~~~
# NLTK has some ready made concordance related objects. In particular, a
# possible solution to the problem could be:
print "Version 3:"
words = nltk.word_tokenize(text)
stemmer = nltk.LancasterStemmer()
c_stemmed = nltk.ConcordanceIndex(words, key=lambda s: stemmer.stem(s.lower()))
print c_stemmed.print_concordance("scared")

# The object offers more convenience functions. The locations for the matches
# are available with the `offsets` method. That allows to collect the words
# that follow the matches for example:
print [words[i+1] for i in c_stemmed.offsets("scared")]
