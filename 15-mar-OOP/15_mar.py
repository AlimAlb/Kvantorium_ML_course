import random as rnd 


#----------------------------------------------------------------------------------------------------------------
# Напишем программу для реализация боя между двумя фантастическими бойцами. Для этого созаддим класс бойца
class Warrior:
    def __init__(self, a, h, m):
        self.attack = a
        self.health = h
        self.meds = m
    def show(self):
        return "attack: " + str(self.attack) + " health: " + str(self.health) + " meds: " + str(self.meds)

    def get_attack(self):
        return self.attack


    def damage(self, damage):
        self.health -= damage
        return self.health > 0


# Создаем объекты двух бойцов класса Warrior 
obj_1 = Warrior(rnd.randint(5, 50), rnd.randint(100, 500), rnd.randint(1, 5))
obj_2 = Warrior(rnd.randint(5, 50), rnd.randint(100, 500), rnd.randint(1, 5))


# Пока один из бойцов не умрет используем метод damage чтобы реализовать битву между ними
i = 0
while obj_1.damage(obj_2.get_attack()) and obj_2.damage(obj_1.get_attack()):
    print("round#", i+1)
    print(obj_1.show())
    print(obj_2.show())
    print()
    i+=1

if obj_1.health <= 0:
    print('second warrior won')
else:
    print('first warrior won')

#----------------------------------------------------------------------------------------------------------------
# Наследование: очень важный концепт в ООП. Наследование позволяет выстроить иерархию классов, где дочерние классы наследуют весь функционал
# родительских классов и при этом могут дополнять его или переопределять.

class Warrior: # <-- класс прородитель
    def __init__(self, lst, a, h, m):
        self.__weapons = lst
        self.__attack = a
        self.__health = h
        self.__meds = m

    def show(self):
        return "attack: " + str(self.__attack) + " health: " + str(self.__health) + " meds: " + str(self.__meds) + " weapons: " + str(self.__weapons)

    def get_attack(self):
        return self.__attack

    def damage(self, damage):
        self.__health -= damage
        return self.__health > 0
    
    def get_weapons(self):
        lst = []
        for item in self.__weapons:
            lst.append(item)
        return lst

class Berserk(Warrior): # <-- дочерний класс
    def __init__(self, lst, a, h, m, s):
        super().__init__(lst, a, h, m)  # super() позволяет обращаться к родительской реализации метода show(), чтобы переопределить его работу в дочернем классе дополнив его вывод
        self.__speed = s

    def get_super_attack(self):
        return self.get_attack() * 1.5

    def show(self):
        return super().show() + " speed: " + str(self.__speed) # super() позволяет обращаться к родительской реализации метода show(), чтобы переопределить его работу в дочернем классе дополнив его вывод

class Kratos(Warrior): # <-- дочерний класс
    def get_rage(self):
        return rnd.randint(1,5) * self.get_attack()

    def show(self):
        return super().show() + " KRATOS"

# Создадим отряд из объектов дочерних классов
squad = []

for i in range(10):
    if rnd.randint(1,2) == 1:
        squad.append(Berserk(['very big sword', 'plash', 'net odnogo glaza'], 1000, 1000, 0, 100))
    else:
        squad.append(Kratos(['blades of ...', 'son'], 2000, 1000, 5))

# Полиморфизм - также ключевой концепт ООП, в двух словах описан ниже - объекты разных классов мы обрабатываем с помощью одного и того же метода show()
# Это можно сделать, так как из-за наследование от общего класса мы можем гарантировать, что в обоих дочерних классах есть такой метод
for item in squad:
    print(item.show())


#----------------------------------------------------------------------------------------------------------------
# Перегрузка операторов

# Мы можем определить работу встроенных функций int(), str(), len(), а также операторов(в том числе арифметических) для нашего класса. 
# Для этого нужно определить работу соотвествующих методов в нашем классе.
class Warrior:
    def __init__(self, lst, a, h, m):
        self.__weapons = lst
        self.__attack = a
        self.__health = h
        self.__meds = m
        self.__lst = lst

    def get_attack(self):
        return self.__attack

    def damage(self, damage):
        self.__health -= damage
        return self.__health > 0
    
    def get_weapons(self):
        lst = []
        for item in self.__weapons:
            lst.append(item)
        return lst

    def __str__(self): # <-- определяет работу str()
        return "attack: " + str(self.__attack) + " health: " + str(self.__health) + " meds: " + str(self.__meds) + " weapons: " + str(self.__weapons)

    def __len__(self): # <-- определяет работу len()
        return len(self.__lst)

    def __getitem__(self, key): # <-- определяет обращение к нашему классу через индекс  - []
        return self.__lst[key]

    def __gt__(self, other): # <-- определяет работу оператора '>'
        return self.__attack + self.__health > other.__attack + other.__attack

    def __add__(self, other): # <-- определяет работу оператора '+'
        return Warrior(self.__lst  + other.__lst, self.__attack  + other.__attack, self.__health  + other.__health, self.__meds  + other.__meds)


# Полный список всех перегружаемых функций и операторов описан тут --> https://pythonworld.ru/osnovy/peregruzka-operatorov.html
        

obj = Warrior(['very big sword', 'plash', 'net odnogo glaza'], 1000, 1000, 10)
obj_1 = Warrior(['very big sword', 'plash', 'net odnogo glaza'], 500, 1000, 10)



s = str(obj)
print(s)
print(len(obj))
print(obj[2])
print(obj > obj_1)
print(obj + obj_1)