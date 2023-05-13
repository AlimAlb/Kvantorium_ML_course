import math

class Vector: 
    def __init__(self, coords_input):
        self.coords = coords_input
        self.shape = len(coords_input)

    def get_coords(self): 
        return self.coords.copy()

    def get_shape(self):
        return self.shape

    def coords_in_square(self): # --> Тимур
        sq = 0
        for i in self.get_coords():
            sq+= i**2
        return sq

    def norm(self): # --> Тимур
        fin = self.coords_in_square() ** 0.5
        return fin

    def normalize(self): # --> Тимур
        new_coords = self.get_coords()
        for i in range(len(new_coords)):
            new_coords[i] = new_coords[i]/self.norm()
        return Vector(new_coords)

    def __add__(self, other): # --> Али
        lst = []
        if type(other) != Vector:
            for i in range(self.get_shape()):
                lst.append(self.get_coords()[i] + other)

            return Vector(lst)


        elif type(other) == Vector:

            if self.get_shape() == other.get_shape():
                for i in range(self.get_shape()):
                    lst.append(self.get_coords()[i] + other.get_coords()[i])
                return Vector(lst)

            if (self.get_shape() != other.get_shape()):
                raise Exception('Shapes of vectors doesnt match')

        else:
            raise Exception('Addition is not defined for this type')

    def __sub__(self, other): # --> Али
        lst = []
        if type(other) != Vector:
            for i in range(self.get_shape()):
                lst.append(self.get_coords()[i] - other)

            return Vector(lst)


        elif type(other) == Vector:

            if self.get_shape() == other.get_shape():
                for i in range(self.get_shape()):
                    lst.append(self.get_coords()[i] - other.get_coords()[i])
                return Vector(lst)

            if (self.get_shape() != other.get_shape()):
                raise Exception('Shapes of vectors doesnt match')

        else:
            raise Exception('Substraction is not defined for this type')

    def __mul__(self, other): # --> Али

        lst = []
        if type(other) != Vector:
            for i in range(self.get_shape()):
                lst.append(self.get_coords()[i] * other)

            return Vector(lst)

    def __truediv__(self, other): # --> Али

        lst = []
        if type(other) != Vector:
            for i in range(self.get_shape()):
                lst.append(self.get_coords()[i] / other)

            return Vector(lst)

    def __pow__(self, other): # --> Али
        pass

    def dot_product(self, other): #--> Тома
        s = 0
        if self.get_shape() != other.get_shape():
            raise Exception('dimensions doen`t match')

        for i in range(self.get_shape()):
            s += other.get_coords()[i]*self.get_coords()[i]
        
        return s

    def cosine(self, other): #--> Тома
        dot_pr = self.dot_product(other)
        a = self.norm()
        b = other.norm()
        r = dot_pr / (a * b)
        return r

    def __iter__(self):
        return iter(self.coords)

#Тома
def read_texts(paths): #[text1.txt, text2.txt ...] --> list of texts(str) 
    pass
    

#Али
def unique_words(lst): #where lst is list of texts --> list of unique words
    pass

unique_word = ['I', 'do', "my", 'homework', 'happy', 'am']


text = 'I do my homework'
vec = [0,0,0,0,0,0]
for i in text.split():
    idx = unique_word.index(i)
    if vec[idx] == 0:
        vec[idx] += 1
    
for i in text.split():
    idx = unique_word.index(i)
    vec[idx] += 1

v = Vector(vec)
v / len(text.split())
        



def vectorize(text, vector_space, vectorization_type):
    
    if vectorization_type == 'count': # Али
        lst = []
        pass 

    elif vectorization_type == 'tf': #Тимур
        pass

    elif vectorization_type == 'tf-idf':# Тома и Тимур
        pass

    else:
        raise Exception("Wrong vectorization type. Should be bool, tf or tf-idf.")


def idf(word, texts):
    count = 0
    if word in texts[0]:
        count += 1
    if word in texts[1]:
        count += 1
    return math.log10(2/count)

# Text 1: I am happy
# [I, am, will, do, my, hw,happy, and, project]
# [1,1,0,0,0,1,0,0]

# term frequency - TF = (number of times word appears in text)/(words in text)



# tf - term frequency 
# idf - inverse document frequency
# is, as, that

# tf = частота слова в тексте / число слов в тексте
# idf = log(всего текстов / тексты где есть это слово)

# tf * idf
# is: 30/200 * 1
# fly: 2/200 * 100