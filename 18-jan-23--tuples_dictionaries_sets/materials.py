#Кортежи - те же списки, только не изменяемые.

tup_1 = (1,2,3,4)

tup_2 = (1,'Name', 3)

print(tup_1, tup_2)

#tup_1[0] = 2 - такое сделать нельзя


#--------------------------------------------------------------------------------------------------------------
#Словари - структура данных, в которой данные храняться в формате ключ-значение. Ключи не могут повторяться.

#key_1 : value_1
#key_2 : value_2


dc = { "name":'Alim', 'surname': 'Albogachiev', 'salary': 100000, 'status': 'manager'} # вот так словарь задается

print(dc['name']) #достать элемент из словаря можно также как и из списка, только вместо индекса - ключ

print(dc['salary']) 

lst = list(dc.keys()) # с помощью метода keys можно достать все ключи словаря
print(lst)

print(dc.values()) # c помощью метода values можно достать все значения из словаря
print(list(dc.values()))

print(dc.items())# c помощью метода items можно достать список из кортежей по два элемента - ключ и значение
lst = list(dc.items())
print(lst[0])

for key in dc.keys(): # есть несколько способов перебрать элементы словаря, выбор зависит от задачи. Можно перебирать поочередно перебирая ключи и по ключу доставая элемент
    print(dc[key])

for value in dc.values(): # либо перебирать напрямую значения
    print(value)

for item in dc.items(): # либо перебирать список из кортежей пар ключ значение
    print(item[0].upper(), item[1])



#Простая программа для учета яблок, бананов и клубники на складе. 
dc = {
    'apple' : 0,
    'strawberry' : 0,
    'bananas' : 0
}
while True: # пока не будет команды остановиться - мы будем считывать строку из названия и количества товаров, а затем будем добавлять количество товаров по соотвествующему ключу
    inp = input('>').split() #bananas 10
    if inp[0] == 'exit':
        break
    dc[inp[0]] += int(inp[1])
    print(dc)



#--------------------------------------------------------------------------------------------------------------
#Множества в питоне являются прямыми аналогами множества из математики. Множества являются не упорядоченными, из него нельзя достать элемент по индексу
#Также множество не хранит дубликатов элементов, любые дублирующиеся элементы будут сводится к одному.

st_1 = set([1,2,3,4,5])
st_2 = set([3,4,5,10,11])

# st1 - st2 = 1,2,3,4,5 - 3,4,5 = 1,2
# st2 - st1 = 10,3,4,5 // 1,2,3,4,5 = 10

print(st_2.intersection(st_1)) # операция пересечения множеств - пересечением {1,2,3,4,5} и {3,4,5,10,11} является множество {3,4,5}
print(st_2.union(st_1)) # операция объединения множеств - объединением {1,2,3,4,5} и {3,4,5,10,11} является множество {1,2,3,4,5,10,11}
print(st_2.difference(st_1))# операция вычитания множеств - разность st2-st1 = {10,11}
print(st_1.difference(st_2))# операция вычитания множеств - разность st1-st2 = {1,2}

#еще примеры операций с множествами: 
fibb = {1,1,2,3,5,8,13,21}
odd = {2,4,6,8,10,12}

print(fibb)
print(odd)

print(fibb.intersection(odd)) # 2,8,
print(fibb.union(odd)) #1,2, ..
print(fibb.difference(odd)) 




#Несмотря на то, что достать конкретный элемент из множества нельзя, все же перебрать все элементы множества
for item in fibb:
    print(item)


#Во время переписи населения часто случались ситуации, когда переписчики записывали одних и тех же людей по несколько раз.
#У нас есть списки людей: Имя|Фамилия|Отчество|год рождения от разных переписчиков. Нужно составить единый список всех людей
#без повторов используя методы set.

print('Введите число переписчиков')
n = int(input('>'))
lst = []
for i in range(n): # для каждого из переписчиков будем собирать его список
    st = set() 
    inp = input('>') 
    while inp != 'stop': #в цикле считываем данные людей пока не будет команды остановиться
        st.add(inp) 
        inp = input('>')

    lst.append(st) # добавляем собранное множество в список

un = lst[0] # возьмем за изначальное множество нулевое из списка
for s in lst[1:]: # будем перебирать все множества из списка и сохранять их объединение с предыдущими
    un = un.union(s)

print(un)
#--------------------------------------------------------------------------------------------------------------
#TODO: Переделать код базы данных под хранение данных в виде словарей.
data_base = []
statuses = ['CEO', 'manager', 'software_engineer']

while True:
    oper = input('>')
    if oper == 'add':
        info = input('>')
        info_lst = info.split('|')
        if not(len(info_lst) == 4):
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
        info_dc = { #все то же самое, только теперь данные о человеке будут храниться в виде словаря и тут мы его создаем
            'name': info_lst[0], 
            'surname': info_lst[1], 
            'salary': info_lst[2], 
            'status': info_lst[3], 
        }
        data_base.append(info_dc) #добавляем словарь с данными в базу данных
    
    if oper == 'delete':
        info = input('>')
        info_lst = info.split('|')
        if not(len(info_lst) == 4):
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

        delete_index = None
        for i in range(len(data_base)):
            if (info_lst[0] == data_base[i]['name'] and 
                info_lst[1] == data_base[i]['surname'] and
                info_lst[2] == data_base[i]['salary'] and
                info_lst[3] == data_base[i]['status']):
                delete_index = i
                break
        data_base.pop(delete_index)



    if oper == 'exit':
        break

    print(data_base)



#--------------------------------------------------------------------------------------------------------------
#На вход программе подаются имена учеников и ряд их оценок. Нужно сохранить все в словарь, посчитать итоговую как среднюю и
#разделить учеников в новый словарь по итоговой оценке.
students = {} 

n = int(input('Введите количество учеников:')) # считываем всех учеников: сначала имена, а потом список оценок ученика.
for i in range(n):
    name = input('Введите имя:')
    lst = []
    for i in range(5):
        lst.append(int(input()))
    students[name] = lst # по ключу имени ученика добавляем как значение список его оценок.

avg = {} 

for item in students.items(): #проходимся по всем парам ключ-значение из словаря с учениками. Для каждого ученика считаем среднюю оценку и создаем словарь средних оценок для каждого ученика
    summ = 0
    for grade in item[1]:
        summ += grade
    avg[item[0]] = summ/len(item[1])

grades = { #словарь с оценками в виде ключей и пустыми списками в виде значений. Мы будем заполнять их именами учеников с соотвествующими оценками
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
}

for key in avg.keys(): # проходим по словарю со средними оценками и по ключу округленной средней оценки добавляем имя ученика в соотвествующий список словаря

    grades[int(round(avg[key], 0))].append(key)

print(grades)

    
#--------------------------------------------------------------------------------------------------------------
#Data base with file(working with files, parser) and dictionaries
#f = open(filename, mode)
# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
# a:  open an existing file for append operation. It won’t override existing data.
# r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.
file = open('file.txt', 'w') # С помощью функции open можно получить доступ к потоку привязанному к файлу в указанном режиме: чтение, запись или дополнение
print(type(file)) # посмотрим тип данных потока



file.write('Some line')#запишем в созданный файл что-то с помощью метода write: он записывает переданную ему строку в файл
file.close()#После завершения работы с файлом поток следует закрыть
file.write('closed') # в закрытый файл уже нельзя ничего писать
file_1 = open('file_1.txt', 'w') #откроем новый файл на запись
file_1.writelines(['Line_1\n','Line_2\n', 'Line_3\n', 'Line_4\n']) # с помощью метода writelines запишем в файл строки из массива
file_1.close() # закроем файл

#доступ на чтение 'w' переписывает данные в файле, если файл ранее существовал. Доступ для дополнения "a" не переписывает старые данные, а дописывает в конец файла.
file = open('file_1.txt', 'a')
file.write('Appended line\n') # добавим строку в конец уже существующего файла
file.close()

#example with r
file = open('file_1.txt', 'r')
print(file.readline()[:-1]) # откроем снова тот же файл и начнем считывать строки поочередно с помощью метода readlines
print(file.readline()[:-1]) # Он каждый раз запоминает где он остановился и с каждым вызовом выдает следующую строку, пока не дойдет до конца файла
print(file.readline()[:-1])
print(file.readline()[:-1])
file.close() 

file = open('file_1.txt', 'r') 
print(file.read()) # c помощью метода read можно прочитать весь файл целиком
file.close()

file = open('file_1.txt', 'r') 
print(file.readlines()) # с помощью метода readlines можно получить список всех строк файла, достаточно удонбый формат
file.close()


