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
word passed are found as well.
"""

import nltk
from string import punctuation

text = nltk.corpus.gutenberg.raw('melville-moby_dick.txt')
