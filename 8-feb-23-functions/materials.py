import math as m

# Повторить чтение из файлов(прошлое занятие), третья домашка остается на след занятие. Поотвечать на вопросы по домашке.
#-------------------------------------------------------------------------------------
# #functions
# def func(a, b): # <- arguments
#     out = a + b
#     return out # <- output value

#TODO: переписать базу данных на функциях


# result = func(3, 4)
# print(result)

# def print_s_n_times(s, n): # <- this function doesnt return anything
#     print(s*n)

# result = print_s_n_times('Hello', 5)
# print(result)

# def print_s_n_times(s, n): # <- this function doesnt return anything
#     print(s*n)
#     return None # <- not a value(blank value)


# result = print_s_n_times('Hello', 5)
# print(result)


#function arguments
#a*c^2*b^3, by default b = 2, c = 3
# def val(a, b =2, c = 3):
#     return a * c**2 * b**3

#-------------------------------------------------------------------------------------
#Nested functions
# e^sin(log(x^2))
# def square(a):
#     return a**2

# def sin(a):
#     return m.sin(a)

#TODO: реализовать небольшую библиотеку для математических функций(для тригонометрических считать самим)
# (tg(cos(sin(x^3-10)))^3 + exp(1/x)^4)/x^5

# a = 10
# result = m.exp(sin(m.log(square(a))))

# print(result)

#Передача функций как объектов, лямбда-функции

#TODO: дополнение функций с помощью передачи функции в функцию в виде аргумента
#TODO: реализовать очередь вызовов функций с возможностью добавления новых
