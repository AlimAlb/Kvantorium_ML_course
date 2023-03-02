#Лямбда функции - пару слов и применение: map, sort by key.

import random as rnd

#ООП

#построить класс какого-нибудь героя из игры

#что такое поля, как их задавать
#что такое конструктор (инициализатор)
#что такое методы класса
#инкапсуляция полей и методов

#Переписать базу данных используя вместо словарей классы, а также базу данных вынести в отдельный класс


#функция принимает коэффиценты a, b, c и возвращает функцию, которая по x считает: ax^2 + bx + c
def get_polynom(a, b, c):
    
    def func(x):
        return a*x**2 + b*x + c

    return func 

#создаем функцию, которая считает 3x^2 + 2x - 1
f = get_polynom(3, 2, -1)
print(f)
print(type(f))
print(f(3))
print(f(5))
print(f(0))


#Лямбда функции: короткий способ объявлять простые функции
#Пример: сделаем функцию, которая считает x^2
sq = lambda x: x**2
print(sq(4))

#Или например, фунцкия принимающая числа a, b и возвращающая a^b
poly = lambda a, b: a**b
print(poly(3, 4))


#Используя лямбда функции перепишем нашу функцию get_polynom
a = 3 
b = 2
c = -1



#Пишем лямбда функцию, которая принимает три аргумента a, b, c и возвращает другую лямбда функцию, которая принимает x и возвращает ax^2 + bx + c 
get = lambda a, b, c: (lambda x: a*x**2 + b*x + c)
func = get(3, 2, -1)
print(func(3))
print(func(5))
print(func(0))
# как видим, работает так же как и get_polynom однако записывается в одну строчку

#---------------------------------------------------------------------------------------------------
#       Объектно-ориентированное программирование - ООП


# Cоздадим класс Warrior, который хранит в себе три параметра: attack, health, meds
class Warrior:
    def __init__(self, a, h, m): # <--- эта штука называется инициализатор, она позволяет вам прописать логику инициализации вашего класса:
        # параметры которые ваш класс принимает при формировании класса и порядок их присвоения
        self.attack = a
        self.health = h
        self.meds = m

    def get_damage(self, damage): # <--- также вы можете прописывать действия, которые можно делать с вашим классом: в нашем случае пропишем 
        # метод get_damage который принимает в себя параметр damage, вычитает его из нашего здоровья и возвращает is_alive - True если живы и False если мертвы
        self.health -= damage
        is_alive = self.health > 0
        return is_alive


obj = Warrior(10,20,5) # Так мы создаем объект класса Warrior. Класс служит некоторым чертежом, планом по которому создаются объекты. 


#Класс объявляется один раз, объектов этого класса может быть бесконечно много.
obj_1 = Warrior(
    10,
    100,
    10
    )

obj_2 = Warrior(100, 2000, 1000)
obj_3 = Warrior(5, 50, 2)

print(obj_1.attack)
print(obj_1.health)
print(obj_1.meds)

#замена параметров в одном объекте не ведет к изменению в других
obj_1.health += 100

print(obj_1.attack)
print(obj_1.health)
print(obj_1.meds)


print(obj_2.attack)
print(obj_2.health)
print(obj_2.meds)


# Cоздадим в цикле 10 объектов нашего класса - небольшой отряд из воинов. Все параметры задаем случайно

squad = []
for i in range(10):
    squad.append(Warrior(
        rnd.randint(10, 100),
        rnd.randint(50, 200),
        rnd.randint(1, 5)
       ))


for i in range(0, 10, 3): # Выведем информацию о каждом воине в отряде
    print('warrior#' + str(i+1))
    print(squad[i].health)
    print(squad[i].attack)
    print(squad[i].meds)

while squad[0].get_damage(10): # Убьем первого воина: для этого в цикле будем вызывать get_damage(10) до тех пор пока он не вернет 
    print(squad[0].health)

print('first warrior is dead')

# Создадим класс для обработки массива данных. Он должен уметь считать:
#-среднее
#-медиана
#-максимум
#-минимум

class Statistics:
    def __init__(self, arr): # внутри объекта храним один параметр - список чисел - массив который анализируем
        self.data = arr
 
    def mean(self): # поиск минимума
        sum = 0
        for item in self.data:
            sum += item
        return sum/len(self.data)
 
    def mediana(self): # поиск медианы
        arr = sorted(self.data)
        if len(arr) % 2 == 0:
            index = len(arr)//2
            return (arr[index] + arr[index-1])/2
            
        else:
            index = len(arr)//2
            return arr[index]


    def min(self): # поиск минимума
        m = self.data[0]
        for i in self.data:
            if i < m:
                m = i
        return m

    def max(self): # поиск максимума
        m = self.data[0]
        for i in self.data:
            if i > m:
                m = i
        return m
 
    def show_arr(self): # напечатать наш список
        print(self.data)


arr = [] 

for i in range(10): # создаем список из 10 случайных чисел
    arr.append(rnd.randint(20, 50))

stats = Statistics(arr) # создаем объект класса Statistics

# проверяем работу
stats.show_arr()
print(stats.mean())
print(sorted(stats.data))
print(stats.mediana())
print(stats.max())
print(stats.min())





#Написать класс который представляет полином степени n. Он должен уметь считать:
#-значение
#-производная


#n, coefs
class Polynom:
    def __init__(self, coefs): # сохраняем один параметр - список коэффицентов при n-ом члене полинома
        self.coefs = coefs

    def value(self, x): # считаем значение в точке x
        sum = 0
        for i in range(len(self.coefs)):
            sum += self.coefs[i] * x**i
        return sum


    def diff(self, x, delta = 0.0001): # считаем производную
        # (f(x + delta) - f(x))/delta
        return (self.value(x + delta) - self.value(x))/delta


#Проверяем работу
pol_2 = Polynom([10,1,1]) # 10 + x + x^2
pol_3 = Polynom([10,1,1,2]) #10 + x + x^2 + 2x^3

print(pol_2.value(5)) 
print(pol_3.value(5))

print(pol_2.diff(5)) # 1 + 2x
print(pol_3.diff(5)) # 1 + 2x + 6x^2

