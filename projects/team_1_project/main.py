from utils import idf, vectorize, unique_words
from vector import Vector
import math

def text_similarity(text1, text2, idfs, top_n = 10):
    un_wrds = unique_words([text1, text2])
    vec1 = vectorize(text1, un_wrds, 'tf-idf', idfs)
    print(vec1) #delete
    vec2 = vectorize(text2, un_wrds, 'tf-idf', idfs)
    print(vec2) #delete
    top_n_valuable_words = most_valuable_words(vec1, vec2, un_wrds, top_n)
    return vec1.cosine(vec2), top_n_valuable_words

def most_valuable_words(v1, v2, unique_words, top_n = 10):
    diff = v1 - v2 
    w_2_v = {}
    # {'I': -0.2, ...}
    for i in range(len(diff)):
        w_2_v[unique_words[i]] = diff.get_coords()[i]
    idx = top_n if top_n < len(w_2_v) else len(w_2_v)
    sorted_w2v = dict(sorted(w_2_v.items(), key=lambda x: math.abs(x[1]), reverse=True) [:top_n if top_n < len(w_2_v) else len(w_2_v)])
    return sorted_w2v



# [(I, -0.2), ...]
# [I, am, happy, will, make, my, projects, and, homework]
# [0.2,0.4,0.4]
# [0.2,0.2,0.6]
# [0, 0.2, -0.2]
    
# t1 = 'I am happy'
# t2 = 'I will make my homework and projects'
# un_w = unique_words([t1, t2])
# idfs = []
# for word in un_w:
#     idfs.append(idf(word, [t1, t2]))

# print(text_similarity(t1, t2, Vector(idfs)))

a = 10
idx = 3 if a < 10 else 100
print(idx)