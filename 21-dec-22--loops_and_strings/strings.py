#slicing
s = 'Hello world!'
print(s[1:5])
print(s[:6])
print(s[3:])
print(s[:-2])
print(s[2:-2])

#Upper/lower
print(s.upper())
print(s.lower())

#index
print(s.index('world'))

#isalnum, isalpha, isdigit, islower, isupper
print('123123asd'.isalnum()) #[a-z] [0-9]
print('123123asd'.isalpha()) #[a-z]
print('123123asd'.isdigit()) #[0-9]
print('asd'.islower())
print('asd'.isupper())

#Проверить,введенные данные: имя, фамилия, номер телефона

#join
print(''.join(['Hello', 'world']))
print(' '.join(['Hello', 'world!']))
print('++++'.join(['Hello', 'world!']))

#Соединить все данные в одну строку: Name: <name>, Surname: <surname>, number: <number>

#split
print("Hello world!".split())
print('Hello,  how are u?'.split())

#Ввод данных в определенном формате и дальнейшее преобразование в формат предыдущего задания
inp = input('Введите имя, фамилию и номер без +:')

lst = inp.split()
error_flag = False

if lst[0].isalpha():
    print('Имя введено верно...')
else:
    print('Ошибка в имени...')
    error_flag = True

if lst[1].isalpha():
    print('Фамилия введена верно...')
else:
    print('Ошибка в фамилии...')
    error_flag = True


if lst[2].isdigit():
    print('номер введен верно...')
else:
    print('Ошибка в номерe...')
    error_flag = True

if not(error_flag):
    out = ' '.join(['Name: ', lst[0], ', Surname: ', lst[1], ', Number: ', lst[2]])
    print(out)


#Форматировнаие





