import math

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
curr = 1
next = 1
n = int(input())
for i in range(n):
    next = curr + next

#mean of n grades for grades in 0 to 5 inputed values without list
n = int(input())
summ = 0
for i in range(n):
    summ += int(input())
mean = summ/n
    


#while loop
a = 0
while a < 5:
    print(a)
    a+=1
#we can any for loop with while:
#fibbonacci number until n-th wih while
curr = 1
next = 1
n = int(input())
i = 0
while i < n:
    next = curr + next
    i+= 1

#input while correct word:
n = input()
while n != 'exit':
    num = int(input())
    print(num**2)
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
inp = input()
flag = True
while flag:
    if inp == 'square':
        print('square: ', int(input())**0.5)
    elif inp == 'quad':
        print('quad: ', int(input())**2)
    elif inp == 'sin':
        print('sin: ', math.sin(int(input())))
    elif inp == 'exit':
        print("Exit.....")
        flag = False
    else:
        print("invalid input, try again:")

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
#sum of 