#-----------------------------------------------------------------------------------------------------
#Кортежи: кортежи по сути своей дублируют по структуре списки, однако главное их отличие - неизменяемость. 
#Ни длину ни отдельные элементы кортежа менять нельзя, у этого есть свои полезные свойства, однако в полной мере мы их
#оценим позже, пока будем считать что кортежи - это более подходящий для предоставления информации вариант, чем списки, 
#так как дает читать информацию, но не дает изменять.

tup = (1,2,3,4)
print(tup)
tup[1] = 0
#-----------------------------------------------------------------------------------------------------
#Словари
#Словари - это структура данных, которая позволяет хранить данные в формате "key" : "value". Ключи, очевидно должны быть уникальны
#Значения - не обязательно
dc = {
    'key_1': 1, 
    'key_2': 10, 
    'key_3': 100
}
dc['key_4'] = 1000
print(dc['key_1'])
print(dc.keys())
print(list(dc.keys()))
print(dc.values())
print(list(dc.values()))
print(dc.items())
print(list(dc.items()))
print()
for key in dc.keys():
    print('key:', key, ", value:", dc[key])
print()
for value in dc.values():
    print(value)
print()
for item in dc.items():
    print(item)
print()
dc.pop('key_2')
print(dc)
#TODO:
#На вход программе подаются имена учеников и ряд их оценок. Нужно сохранить все в словарь, посчитать итоговую как среднюю и
#разделить учеников в новый словарь по итоговой оценке.



#TODO:
#переписать базу данных под словари
#Добавить возможность кастомных полей
#-----------------------------------------------------------------------------------------------------
#Sets
st_1 = set([('1', '2'), ('2', '3'), ('2', '4'), ('1', '7')])
st_2 = set([('2', '2'), ('2', '3'), ('0', '4'), ('1', '7')])

print(st_2.intersection(st_1))
print(st_2.intersection(st_1))
print(st_2.difference(st_1))
#Во время переписи населения часто случались ситуации, когда переписчики записывали одних и тех же людей по несколько раз.
#У нас есть списки людей: Имя|Фамилия|Отчество|год рождения от разных переписчиков. Нужно составить единый список всех людей
#без повторов используя методы set.
#-----------------------------------------------------------------------------------------------------
#Data base with file(working with files, parser) and dictionaries
#f = open(filename, mode)
# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
# a:  open an existing file for append operation. It won’t override existing data.
# r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.
file = open('file.txt', 'w')
print(type(file))

#write something
file.write('Some line')#writes string to file
file.close()#CLOSE FILES
#file.write('closed') # u cant write in closed file
file = open('file_1.txt', 'w')
file.writelines(['Line_1\n','Line_2\n', 'Line_3\n', 'Line_4\n'])
file.close()

#example with a
file = open('file_1.txt', 'a')
file.write('Appended line\n')
file.close()

#example with r
file = open('file_1.txt', 'r')
print(file.readline()[:-1])
print(file.readline()[:-1])
print(file.readline()[:-1])
print(file.readline()[:-1])
file.close()

#simple parser
row = {
        'name': 'Alim', 
        'surname': 'Albogachiev', 
        'salary': 20000, 
        'status': 'teacher'
        }
columns = list(row.keys())
data = [row['name'], row['surname'], str(row['salary']), row['status']]
file = open('db.txt', 'a')
file.write('|'.join(columns) + '\n')
file.write('|'.join(data) + '\n')
file.close()

#read
file = open('db.txt', 'r')
columns = file.readline()[:-1].split('|')
print(columns)
data = file.readline()[:-1].split('|')
print(data)

#TODO: Реализовать базу данных на произвольных колонках с возможностью удаления и добавления элементов

#Nested dictionaries
company_structure = {
    'marketing':{
        'director': { 'name': 'John', 'surname': 'Snnerman', 'salary': 120000}, 
        'manager_1': { 'name': 'Hon', 'surname': 'Son', 'salary': 60000}, 
        'manager_1': { 'name': 'Arnold', 'surname': 'Ravovsky', 'salary': 60000}, 
    }, 
    'IT':{
        'team lead': { 'name': 'Ann', 'surname': 'Kindy', 'salary': 250000}, 
        'engineer_1': { 'name': 'Dag', 'surname': 'Adamson', 'salary': 100000}, 
        'engineer_2': { 'name': 'Denis', 'surname': 'Sink', 'salary': 100000}, 
        'engineer_3': { 'name': 'Arnold', 'surname': 'Ravovsky', 'salary': 100000}, 
    }, 
    'analytics':{
        'Team Lead': { 'name': 'Ser', 'surname': 'Qwerty', 'salary': 150000}, 
        'analytic_1': { 'name': 'Fill', 'surname': 'Sata', 'salary': 120000}, 
        'analytic_2': { 'name': 'Virgil', 'surname': 'Snyder', 'salary': 120000}, 
    }
}

for key in company_structure:
    print(company_structure[key])