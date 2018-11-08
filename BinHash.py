
"""
    BinHash.py
    
    Usage:

    >>> from BinHash import hasher
    >>> corpus = 'path_to_the_folder_containing_documents'
    >>> d = 10000
    >>> k = 500
    >>> myhasher = hasher(corpus, d, k)
    >>> sample_text = "this is a sample text"
    >>> sample_hash = myhasher.hash_text(sample_text)

"""


class hasher():
    def __init__(self, corpus='wiki', d=10000, k=500):
        pass

    def hash_text(self, text):
        pass

    
