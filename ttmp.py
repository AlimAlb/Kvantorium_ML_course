
d = {'read': "R", 'write': "W", 'run': "X"}
d2 = {"R": 'доступно для чтения',
      "W": 'доступно для записи',
      "X": 'доступ к запуску'}

file = open('access.txt', encoding='utf-8')
file_access = file.readlines()
while True:
    item = input("Введите операцию (run, read, write) и файл,[exit - чтобы выйти из проги]: ").split()

    if item[0] == 'exit':
        break


    for i in file_access:
        if i.split()[0] == item[1]:
            if d[item[0]] in i.split():
                print(d2[d[item[0]]])
            else: 
                print('доступ отклонён' , end='')

file.close()

