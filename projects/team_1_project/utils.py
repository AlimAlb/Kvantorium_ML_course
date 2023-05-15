from vector import Vector
import math




def unique_words(lst):
    lst_un_word = []
    for text in lst:
        words = text.split()
        for word in words:
            if word not in lst_un_word:
                lst_un_word.append(word)
    return lst_un_word

def idf(word, texts):
    count = 0
    if word in texts[0].split():
        count += 1
    if word in texts[1].split():
        count += 1
    return math.log(2/(count)) + 1

def tf(text, vector_space):
    tokens = text.split()
    vec = []
    for i in range(len(vector_space)):
        vec.append(0)
    for token in tokens:
        #[0,0,0,0,0,0,0,0,0]
        idx = vector_space.index(token)
        vec[idx] += 1
        
    vector = Vector(vec)
    return vector / len(tokens)

def vectorize(text, vector_space, vectorization_type, idfs = None):
    
    if vectorization_type == 'count':
        liist = []
        for i in range(len(vector_space)):
            liist.append(0)

        for z in text.split():
            idx = vector_space.index(z)
            if liist[idx] == 0:
                liist[idx] += 1
        return Vector(liist)

    elif vectorization_type == 'tf':
        return tf(text, vector_space)
        
    elif vectorization_type == 'tf-idf':
        if type(idfs) != Vector:
            raise Exception("There is no idfs")
        
        term_f = tf(text, vector_space)
        
        return term_f * idfs

    else:
        raise Exception("Wrong vectorization type. Should be bool, tf or tf-idf.")
