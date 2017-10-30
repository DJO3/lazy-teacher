"""
Common functions for cleaning and indexing text
"""
import re


def sanitize(text):
    """
    Strips all non alphabetical characters and white space from text
    """

    # Sanitize results
    stripped_text = re.sub(r'([^\s\w]|_)+', '', str(text, 'utf-8'))
    clean_text = re.sub(r'[\n|\r]', ' ', stripped_text)

    return clean_text

def count(text, min_length=2):
    """
    Indexes a count of all words found in text
    """

    index = {}
    for word in text.split(" "):
        if index.get(word.lower()):
            index[word.lower()] += 1
        elif len(word) >= min_length:
            index[word.lower()] = 1

    return index
