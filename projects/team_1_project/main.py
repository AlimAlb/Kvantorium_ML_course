from utils import idf, vectorize, unique_words
from vector import Vector
import math

def text_similarity(text1, text2, idfs, top_n = 10):
    un_wrds = unique_words([text1, text2])
    vec1 = vectorize(text1, un_wrds, 'tf-idf', idfs)
    vec2 = vectorize(text2, un_wrds, 'tf-idf', idfs)
    top_n_valuable_words = most_valuable_words(vec1, vec2, un_wrds, top_n)
    return vec1.cosine(vec2), top_n_valuable_words

def most_valuable_words(v1, v2, unique_words, top_n = 10):
    diff = v1 - v2 
    w_2_v = {}
    # {'I': -0.2, ...}
    for i in range(len(diff)):
        w_2_v[unique_words[i]] = diff.get_coords()[i]
    idx = top_n if top_n < len(w_2_v) else len(w_2_v)
    sorted_w2v = dict(sorted(w_2_v.items(), key=lambda x: abs(x[1]), reverse=True) [:idx])
    return sorted_w2v


def analyzer(text1, text2, top_n = 10):
    un_w = unique_words([text1, text2])
    idfs = []
    for word in un_w:
        idfs.append(idf(word, [text1, text2]))
    
    return text_similarity(text1, text2, Vector(idfs), top_n)

    



    
t1 = 'I am happy'
t2 = 'I will make my homework and projects'


print(analyzer(t1, t2))



