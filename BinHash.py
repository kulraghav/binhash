
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

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from os import listdir
from os.path import join, isfile
import re

def preprocess(text):

    text = text.lower()
    text = text.replace("\n", " ")
    text = re.sub('[^0-9a-zA-Z]+', ' ', text)    
    text = " ".join(text.split(" "))

    return text
    
def build_corpus(path_to_docs):

    corpus=[]
    paths = [join(path_to_docs, filename) for filename in listdir(path_to_docs) if isfile(join(path_to_docs, filename)) and filename[-4:] == '.txt']
    
    for path in paths:
        with open(path, "r") as f:
            lines = f.readlines()
            text = preprocess(" ".join(lines))
            corpus.append(text)

    return corpus

def get_top_words(corpus, d):
    
    if type(corpus) == 'string':
        corpus = build_corpus(corpus)

    vectorizer = TfidfVectorizer()
    vectorizer.fit_transform(corpus)
    features = vectorizer.get_feature_names()

    top_words = {}
    for i in range(d):
        top_words[features[i]] = i

    return top_words

def get_bucket_mapping(d, k):
    buckets = {}
    for i in range(d):
        r = randint(0, k-1)
        buckets[i] = r

    return buckets    

class hasher():
    def __init__(self, corpus='wiki', d=10000, k=500):
        self.d = d
        self.k = k
        self.words =  get_top_words(corpus, d)        
        self.buckets = get_bucket_mapping(d, k)      
    

    def hash_text(self, text):

        binary_hash = []
        for i in range(k):
            binary_hash[i] = 0
         
        tokens = preprocess(text).split(" ")

        for token in tokens:
            binary_hash[buckets[words[token]]] = 1

        return binary_hash        
        
        
                

    
