import math

class Vector: 
    def __init__(self, coords_input):
        self.coords = coords_input
        self.shape = len(coords_input)

    def get_coords(self): 
        return self.coords.copy()

    def get_shape(self):
        return self.shape

    def coords_in_square(self): 
        sq = 0
        for i in self.get_coords():
            sq+= i**2
        return sq

    def norm(self): 
        fin = self.coords_in_square() ** 0.5
        return fin

    def normalize(self): 
        new_coords = self.get_coords()
        for i in range(len(new_coords)):
            new_coords[i] = new_coords[i]/self.norm()
        return Vector(new_coords)

    def __add__(self, other): 
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

    def __sub__(self, other): 
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

    def __mul__(self, other): 
        lst = []
        if type(other) != Vector:
            for i in range(self.get_shape()):
                lst.append(self.get_coords()[i] * other)

            return Vector(lst)
        
        if type(other) == Vector:
            new_vec = []
            for i in range(self.get_shape()):
                new_vec.append(self.get_coords()[i] * other.get_coords()[i])
            return Vector(new_vec)

    def __truediv__(self, other):

        lst = []
        if type(other) != Vector:
            for i in range(self.get_shape()):
                lst.append(self.get_coords()[i] / other)

            return Vector(lst)
 
    def dot_product(self, other): 
        s = 0
        if self.get_shape() != other.get_shape():
            raise Exception('dimensions doen`t match')

        for i in range(self.get_shape()):
            s += other.get_coords()[i]*self.get_coords()[i]
        
        return s

    def cosine(self, other): 
        dot_pr = self.dot_product(other)
        a = self.norm()
        b = other.norm()
        r = dot_pr / (a * b)
        return r

    def __iter__(self):
        return iter(self.coords)
    
    def __len__(self):
        return self.get_shape()

    def __str__(self):
        return f"Vector({self.get_coords()})"




