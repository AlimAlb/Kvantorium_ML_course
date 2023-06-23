
# text = input()
# shifr_dc = {}
# inp = input()

# while inp != 'end':
#     tmp = inp.split(' - ')
#     shifr_dc[tmp[0]] = tmp[1]
#     inp = input()

# text_lst = text.split()
# shifred_lst = []

# for word in text_lst:
#     shifred_lst.append(shifr_dc[word])

# shifred_text = ' '.join(shifred_lst)

# print("SHIFRED TEXT: " + shifred_text)

# out = open('shifr.txt', 'w')
# out.write(shifred_text)
# print("Text shifred")
# out.close()

# inp = open('shifr.txt', 'r')
# after_shifr = inp.read()

# unshifr_dc = {}

# for key in shifr_dc.keys():
#     unshifr_dc[shifr_dc[key]] = key


# unshifred_lst= []
# shifred_lst = shifred_text.split()
# for word in shifred_lst:
#     unshifred_lst.append(unshifr_dc[word])

# unshifred_text = " ".join(unshifred_lst)

# print("DESHIFRED TEXT: " + unshifred_text)


# dc = {
#     'run' : 'X', 
#     'read': 'R', 
#     'write': 'W'
# }

# def is_allowed(command, file, access):
#     for key in access.keys():
#         if key == file:
#             if dc[command] in access[key]:
#                 return True
#             else:
#                 False

# file = open("access.txt", 'r')
# access = file.readlines()
# access_dc = {}

# for line in access:
#     tmp = line.split()
#     access_dc[tmp[0]] = tmp[1:]
#     #'split.py'              'W', 'X', 'R'

# inp = input()
# while True:
#     if inp == 'EXIT':
#         break

#     tmp = inp.split()

#     if is_allowed(tmp[0], tmp[1], access_dc):
#         if tmp[0] == 'run':
#             print('...execution started...')
#         elif tmp[0] == 'read':
#             print('...reading allowed...')
#         elif tmp[0] == 'write':
#             print('...writing allowed...')
#     else:
#         print('...access denied...')

#     inp = input()





# print("...END OF EXECUTION...")


# tmp = '2 +3 /4 *10 -100'

# spt = tmp.split()

# add = lambda a, b: a + b
# dif = lambda a, b: a - b
# mul = lambda a, b: a * b
# div = lambda a, b: a / b

# curr = int(spt[0])
# for i in range(1, len(spt)):
#     if spt[i][0] == '+':
#         curr = add(curr, int(spt[i][1:]))
#     if spt[i][0] == '-':
#         curr = dif(curr, int(spt[i][1:]))
#     if spt[i][0] == '*':
#         curr = mul(curr, int(spt[i][1:]))
#     if spt[i][0] == '/':
#         curr = div(curr, int(spt[i][1:]))

# print(curr)


def func(a, b, c):
    def f(x):
        return a*x**2 + b*x + c

    return f

def diff(f, x, delta = 0.000000001):
    fdelta = f(x + delta)
    fx = f(x)
    df = (fdelta - fx)/delta
    return df


#f_curr - f_last > 0.001


#x = x - step*diff(x)

# y = x^2 + 2x + 1
y = func(1,2,1)

#ax^2 + bx + c
#2ax + b


#print(y(5))

print(diff(y, 2))


# y' = 2x + 2 = 4 + 2 = 6



    
    

















        


