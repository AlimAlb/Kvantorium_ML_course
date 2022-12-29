#Определение и индексация списков
lst = [ 
    1,#0 -5
    2,#1 -4
    3,#2 -3
    4,#3 -2 
    5 #4 -1 
    ]

lst_1 = [1,2,3,4]
lst_2 = ['one', 'two', 'three']
lst_3 = ['one', 2, 3.5]
lst_emp = [] 
print(lst_1)
print(lst_2)
print(lst_3)
print(lst_emp)

#-----------------------------------------------------------
#indexes and slices
lst = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']

print(lst[0], lst[2], lst[-1], lst[-2])
print(lst[:2])
print(lst[2:6])
print(lst[2:-1])
print(lst[2:4])
print(lst[2:5:2])
print(lst[5:2:-1])
print(lst[:2:-1])

#Работа со спискаки в цикле:
for i in range(len(lst)):  #<-- [0,1,2,3,4,5,6]
    print(lst[i])

for i in range(len(lst)): #<-- [0,1,2,3,4,5,6]
    print(lst[i]*(i+1))
#-----------------------------------------------------------
# Есть две списка: вес и единица измерения. Суммарный вес всех посылок в кг
weights = [3.5, 4.2, 6.8, 7.2, 4.3, 9, 8.8, 9.1, 20, 1, 15.6]
weight_class = ['kg', 'lbs', 'kg', 'kg', 'lbs', 'tons', 'centners', 'lbs', 'centners', 'lbs', 'kg']

lbs_to_kg = 0.45

summ = 0

for i in range(len(weights)):
    if weight_class[i] == 'kg':
        summ += weights[i]
    elif weight_class[i] == 'lbs':
        summ += lbs_to_kg*weights[i]
    elif weight_class[i] == 'tons':
        summ += 1000*weights[i]
    elif weight_class[i] == 'centners':
        summ += 100*weights[i]

print('Сумма всех посылок: ', round(summ, 2), 'кг.')
#-----------------------------------------------------------
#Списки можно складывать
lst_1 = [1,2,3,4]
lst_2 = [10,11,12,13]

print(lst_1 + lst_2)
#-----------------------------------------------------------
#in key-word 
print(1 in [1,2,3,4])
print('ab' in 'abcd')
print('f' in 'abcd')
print(5 in [1,2,3,4])

#for-loop with in key-word
for weight in weights:
    weight += 1
    print(weight)

#-----------------------------------------------------------
#upraged weights counter
weights = []
weight_class = []
print('Введите количество посылок на складе:')
n = int(input('>'))

w_classes = ['kg', 'centners', 'tons', 'lbs']
i = 0
print('Вводите вес и единицу измерения в формате <вес>|<единица измерения>:')
while i < n:
    inp = input('>')
    lst = inp.split('|')
    if not(len(lst) == 2):
        print('wrong input...')
        continue    
    if not(lst[0].isdigit()):
        print('weight is not integer...')
        continue
    if not(lst[1] in w_classes):
        print('weight class is wrong...')
        continue
    weights.append(int(lst[0]))
    weight_class.append(lst[1])

    i += 1

summ = 0

for i in range(len(weights)):
    if weight_class[i] == 'kg':
        summ += weights[i]
    elif weight_class[i] == 'lbs':
        summ += lbs_to_kg*weights[i]
    elif weight_class[i] == 'tons':
        summ += 1000*weights[i]
    elif weight_class[i] == 'centners':
        summ += 100*weights[i]

print('Сумма всех посылок: ', round(summ, 2), 'кг.')
#-----------------------------------------------------------
#Data base with lists
#info = ['Name', 'Surname', 10000, 'status']
#data_base = [['Name', 'Surname', 10000, 'status'], ['Name', 'Surname', 10000, 'status'], ['Name', 'Surname', 10000, 'status']]
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
        data_base.append(info_lst)
    
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
            if (info_lst[0] == data_base[i][0] and 
                info_lst[1] == data_base[i][1] and
                info_lst[2] == data_base[i][2] and
                info_lst[3] == data_base[i][3]):
                delete_index = i
                break
        data_base.pop(delete_index)



    if oper == 'exit':
        break

    print(data_base)
