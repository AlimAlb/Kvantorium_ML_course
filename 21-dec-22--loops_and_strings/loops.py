import math


#range(start, stop, step)
print(range(10))

print(range(10)[2])

print(list(range(10)))

print(list(range(2,10, 3)))

print(list(range(10,2, -2)))


for i in range(10):
    print(i)

for i in range(2, 10, 3):
    print(i)

for i in range(10, 2, -1):
    print(i)

#summ for every odd number for 0 to 20
summ = 0
for i in range(0, 20, 2):
    summ += i

summ = 0
for i in range(20):
    if i % 2 == 0:
        summ += i

#fibbonacci number until n-th
curr_1 = 1
curr_2 = 1
n = int(input())
for i in range(2, n):
    curr_2 = curr_1 + curr_2
    curr_1 = curr_2 - curr_1
print(curr_2)

#mean of n grades for grades in 0 to 5 inputed values without list
n = int(input('Введите количество оценок: '))
summ = 0
for i in range(n):
    grade = int(input())
    summ += grade

print("Средний балл равен: ", summ/n)
    


#while loop
a = 0
while a < 5:
    print(a)
    a+=1
#we can any for loop with while:
#fibbonacci number until n-th wih while
curr_1 = 1
curr_2 = 1
n = int(input())
i = 0
while i + 2 < n:
    curr_2 = curr_1 + curr_2
    curr_1 = curr_2 - curr_1
    i += 1

print(curr_2)

#input while correct word:
n = input()
while n != 'exit':
    print(int(n)**2)
    n = input()
#grades with loop and input till correct
n = int(input())
summ = 0
i = 0
while i < n:
    grade = int(input())
    if grade < 0 or grade > 5:
        print('invalid grade, try again')
    else:
        summ += int(input())
        i+= 1
mean = summ/n
#simple console menu with while loop
import math
#while exit - squared numbers
end_flag = False
#**2
#sqrt
#sin
print("use three operations:\n1. power\n2. sqrt\n3. sin\n")
while not(end_flag):
    path = input('operation:')
    if path == 'power':
        print(int(input('number:'))**2)
    elif path == 'sqrt':
        print(int(input('number:'))**0.5)
    elif path == 'sin':
        print(math.sin(int(input('number:'))))
    else:
        print('invalid operation...')
        end_flag = True

#break
#break statement allows us stop loop under some conditionbs
for i in range(10):
    if i == 5:
        break
    print(i)

#sum of n numbers
counter = 0
n = int(input())
while True:
    sum += int(input())
    if counter == n:
        print('end of sum....')
        print('sum: ', sum)
        break

#continue
#continue statement allows us to skip iteration of loop under some conditions
#sum of odd numbers:
summ = 0
for i in range(20):
    if i % 2 != 0:
        continue
    sum += i

#squares of numbers that devides by 3
for i in range(20):
    if i % 3 != 0:
        continue
    print(i**2)

#_in_ key word
