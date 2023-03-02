#переписать базу данных на функциях и файлах
#задачка с производной - объяснить и показать что функция - тоже объект, лямбда функции


#ДЗ
#добавить задачку на лямбда функции

#ООП - начало:
#-что такое класс
#-что такое поле
#-что такое метод
#-что такое конструктор
#-



#Перепишем базу данных: вынесем все в функции и добавим чтение и запись файла
import os


data_base = []
statuses = ['CEO', 'manager', 'software_engineer']

{
    'name': 'Alim',
    'surname': 'Albo',
    'salary': 2000,
    'status' : 'CEO'
}

#readline
#read
#readlines

#write
#writelines

def input_data():
    while True:
        info = input('>')
        info_lst = info.split('|')
        if len(info_lst) != 4:
            print('Error: wrong_format')
            continue
        if not(info_lst[0].isalpha()):
            print('Error: wrong_name')
            continue
        if not(info_lst[1].isalpha()):
            print('Error: wrong_surname')
            continue
        if not(info_lst[2].isdigit()):
            print('Error: wrong_salary')
            continue
        if not(info_lst[3] in statuses):
            print('Error: wrong_status')
            continue
        info_lst[2] = int(info_lst[2])
        info_dc = {
            'name': info_lst[0], 
            'surname': info_lst[1], 
            'salary': info_lst[2], 
            'status': info_lst[3], 
        }
        return info_dc

def to_str(dc):
    tmp = list(dc.values())
    tmp[2] = str(tmp[2])
    return '|'.join(tmp)

def show(data_base):
    for i in range(len(data_base)):
            print(to_str(data_base[i]))


def delete(db):
    delete_info = input_data()
    delete_index = None
    for i in range(len(data_base)):
        if (delete_info['name'] == db[i]['name'] and 
            delete_info['surname'] == db[i]['surname'] and
            delete_info['salary'] == db[i]['salary'] and
            delete_info['status'] == db[i]['status']):
            delete_index = i
            break
    db.pop(delete_index)

def add(db):
    db.append(input_data())
    
def write_db(db):
    lines = []
    for i in range(len(db)):
        lines.append(to_str(db[i]) + '\n')

    file = open('db.txt', 'w')
    file.writelines(lines)
        
        
def read_db(db):
    if not(os.path.exists('db.txt')):
        file = open('db.txt', 'w')
        file.close()

    else:
        file = open('db.txt', 'r')
        lines = file.readlines()
        for line in lines:
            info_lst = line.split('|')
            info_lst[2] = int(info_lst[2])
            info_dc = {
                'name': info_lst[0], 
                'surname': info_lst[1], 
                'salary': info_lst[2], 
                'status': info_lst[3][0:-1], 
            }
            db.append(info_dc)


#reading
read_db(data_base)
print('.....reading.....')
while True:
    oper = input('>')

    if oper == 'add':
        add(data_base)
    
    if oper == 'delete':
        delete(data_base)

    if oper == 'show':
        show(data_base)

    if oper == 'exit':
        write_db(data_base)
        print('.....writing.....')
        break

#------------------------------------------------------------------------------------------------------------------------------

# В питоне функции также являются объектами: их можно присваивать в переменные, делать из них списки
def pow(a,b):
    return a**b

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def func(f, a, b): # функция принимает три параметра: f - некая функция, a, b - ее аргументы, а затем вызывает функцию с аргументами a,b
    return f(a,b)

lst = [pow, add, mul] # создадим список из 3 функций
 
for f in lst:   # проходимся по списку из функций, передаем их поочередно в функцию func которая их вызывает и возвращает результат вызова с аргументами a = 2,b = 3
    print(func(f, 2, 3))


#------------------------------------------------------------------------------------------------------------------------------------------------------

#Рассмотрим задачу №2 из ДЗ №4 - поиск минимума квадратичной функции



#функция quad принимает три аргумента - a,b,c и возвращает функцию f(x) которая принимает один параметр x и возвращает - ax^2 + bx + c 
def quad(a,b,c):
    def f(x):
        return a*x**2 + b*x + c

    return f 

# функция diff принимает три параметра - f, x, delta, f - дифференцируемая функция, x - точка в которой считаем производную, delta - dx - шаг на который отсупаем
def diff(f, x, delta = 0.00000001):
    return (f(x+delta) - f(x))/delta



a = int(input())
b = int(input())
c = int(input())

func_4 = quad(a,b,c) #создаем функцию, которая возвразает ax^2 + bx + c

print(diff(func_4, 2)) # считаем ее производную в точке 2