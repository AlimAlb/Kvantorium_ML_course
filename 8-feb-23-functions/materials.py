# #Чтение и запись в файл, основы
# file = open('file.txt', 'w') # create
# print(type(file))

# file.write('Some line\n') # working with file
# file.close()
# file = open('file.txt', 'a')
# file.write('Other line')
# file.close() # close


# #readline
# file = open("coefs.txt", 'r')
# print(file.readline()[:-1]) #1 2 3\n
# print(file.readline()[:-1]) # выдает по одной строчке из файла поочередно
# print(file.readline()[:-1]) 
# file.close()


# #read
# file = open("coefs.txt", 'r')
# s = file.read()
# s_2 = file.read()
# print(file.read())
# print(file.read())
# print(s[1])
# print(s[10])
# file.close()

# #readlines
# file_coefs = file = open("coefs.txt", 'r')
# print(file.readlines()) #выдает список из строк в файле

# coef_s = file_coefs.readlines()
# coefs = []

# #functions inputs and coefs
# # ax^2 + bx + c 
# #coefs.txt
# # 1 2 3 
# # 3 2 4
# # ...

# # 1*x^2 + 2*x + 3

# #x.txt
# # 1
# # 10
# # 18 
# # 5

# for i in range(len(coef_s)):
#     coef_s[i] = coef_s[i][:-1]
#     coef = coef_s[i].split()

#     for j in range(len(coef)):
#         coef[j] = int(coef[j])
    
#     coefs.append(coef)

# # # [[1,2,3], [3,4,1] ....]

# file_x = open('x.txt', 'r')
# x_s = file_x.readlines()
# x = []

# for i in range(len(x_s)):
#     x_s[i] = x_s[i][:-1]
#     x.append(int(x_s[i]))


# for i in range(len(coefs)): # перебор всех коэффицентов
#     file = open('file' + str(i+1) + '.txt', 'w')
#     for j in range(len(x)): # перебор всех x
#         out = coefs[i][0]*x[j]**2 +  coefs[i][1]*x[j] + coefs[i][2]
#         file.write(str(out) + '\n')
#         #ax^2 + bx + c 
#     file.close()


    

# file_x.close()
# file_coefs.close()

# #----------------------------------------------------------------------------------------
# #Функции

# # ax^2 + bx + c
# def func(x, a, b, c):
#     out = a*x**2 + b*x + c
#     return out

# out = func(10, 1,2,3)
# # 1*0^2 + 2*0 + 3
# print(out)

# def add_hello(s):
#     print('hello, ' + s)

# out = add_hello('Alim')
# print(out)
# None


# #------------------------------------------------------------------------------------------
# #Напишем функции для приближенного вычисления математических функций
# def factorial(x):
#     curr = 1
#     for i in range(0, x):
#         curr *= (i+1)
#     return curr


# def exp(x): # e^x
#     out = 1 +   x + x**2/factorial(2) + x**3/factorial(3)
#     return out
    

# def sin(x):
#     out = x - x**3/factorial(3) + x**5/factorial(5)
#     return out

# def cos(x):
#     out = 1 - x**2/factorial(2) + x**4/factorial(4)
#     return out

# def tg(x):
#     return sin(x)/cos(x)


# print(exp(0))
# print(exp(1))

# print(sin(0))
# print(sin(1.57))

# print(cos(0))
# print(cos(1.57))

# print(tg(0.8))

# print(factorial(1))
# print(factorial(3))
# print(factorial(5))


#------------------------------------------------------------------------------------------
