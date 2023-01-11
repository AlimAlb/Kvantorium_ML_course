#--------------------------------------------------------------------
#Пояснение к задаче с векторами. Один из возможных шаблонов решения.
print('Программа для работы с векторами')
print('+ - for adding')
print('* - for adding')
print('norm - for adding')
while True:# бесконечный цикл, который прерывается только если пользователь вводит exit
    inp = input()
    if inp == 'exit': #то самое прерывание 
        break

    if inp == "+": # в случае если вводят плюс, тут нужен код для сложения векторов
        #сложение 
        print('...adding...')
    if inp == "*": # в случае если вводят скалярное умножение, тут нужен соотвествущий код тоже
        #сложение
        print('...mult...')
    if inp == "norm": # ну и норма
        #сложение 
        print('...norm...')

#--------------------------------------------------------------------
#Один из возможных шаблонов для задачи с цензурированием текста. 
text = input()
bad_words =  ['assad', 'kumbro', 'kilatra', 'saluki', 'oudolu', 'lavida', 'seotida']
words = text.split() # разбиваем текст на отдельные слова и проверяем по одному слову
clean_text = []
for word in words:
    for bad_word in bad_words:
        word == bad_word
    #is_aplha - по этим фукнциям информация есть в материалах соотвествующего занятия
    #is_lower   

    clean_text.append(word)

out = ' '.join(clean_text)
print(out)

#--------------------------------------------------------------------
#Тут разбирали задачу с базой данных, лучше посмотреть запись.

data_base = []
statuses = ['CEO', 'manager', 'software_engineer']

while True:
    oper = input('>')
    if oper == 'add':
        info = input('>')
        info_lst = info.split('|')
        print(info_lst)
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
        #проверить, что данные не повторяются (пройтись циклом по базе данных и проверить что такого элемента нет)
        
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

    if oper == 'show':
        #Name--Surname--Salary--Status
        print('...showing...')



#--------------------------------------------------------------------
#Задача с выводом всех четных чисел от n до нуля
n = int(input('Введите число:'))
n = (n//2)*2 # эта строчка сделает число n равным ближайшему(меньшему) четному числу. Например: 101//2 = 50, 50*2 = 100

#Далее просто от этого четного числа двигаемся назад с шагом два и выводим четные числа
for i in range(n, 1, -2): 
    print((i)**2)

