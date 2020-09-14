# print('Teste 1')
# z = 10
# y = 0
# x = y < z and z > y or y > z and z < y
# print(x)
#
# print('Teste 2')
# x = 1
# x = x == x
# print(x)
#
# print('\nTeste 3')
# lst1 = [1, 2, 3]
# lst2 = []
# for v in lst1:
#     lst2.insert(0, v)
# print(lst2)
#
# print('\nTeste 4')
# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
# print(c + d + e)
#
# print('\n Teste 5')
# nums = [1, 2, 3]
# vals = nums
# del vals[1:2]
# print(nums)
# print(vals)
#
# print('\nTeste 6')
# lst = [1, 2, 3]
# for v in range(len(lst)):
#     lst.insert(1, lst[v])
# print(lst)
#
# print('\nTeste 7')
# for i in range(1):
#     print('#')
# else:
#     print('#')
#
# print('\nTeste 8') # errei
# i = 0
# while i <= 5:
#     i += 1
#     if i % 2 == 0:
#         break
#     print('*')
#
# print('\nTeste 9')
# lst = [3, 1, -2]
# print(lst[lst[-1]])
#
# print('\nTeste 10') # errei
# nums = [1, 2, 3]
# vals = nums[-1:-2]
# print(nums)
# print(vals)

# print('\nTeste 11') # errei
# lst = [[0, 1, 2, 3] for i in range(2)]
# print(lst[2][0])

# nums = [1, 2, 3]
# vals = nums
# del vals[1:2]
# print(vals)
# print(nums)

# lst = [1, 2, 3, 4]
# print(lst[-3:-2])

# nums = [1, 2, 3]
# vals = nums[-1: -2]
# print(nums)
# print(vals)

# print('Qts * são impressos')
# i = 0
# while i <=5:
#     i +=1
#     if i % 2 == 0:
#         break
#     print('*')

# print('Qual é o output?')
# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
# print(c + d + e)

# print('A soma dos valores de vals ao final é?')
# vals = [0, 1, 2]
# vals.insert(0, 1)
# del vals[1]
# print(vals)

# lst = [i for i in range(-1, 2)]
# print(lst)

# print('Quantos # serão impressos?')
# for i in range(1):
#     print('#')
# else:
#     print('#')

# print('Quantos # serão impressos?')
# var = 1
# while var < 10:
#     print('#')
#     var = var << 1
#     print(var)

# list = ['Mary', 'had', 'a', 'little', 'lamb']
# def list(lst):
#     del lst[3]
#     lst[3] = 'ram'
# print(list(list))

# dct = {}
# lst = ['a', 'b', 'c', 'd']
# for i in range(len(lst) - 1):
#     dct[lst[i]] = (lst[i], )
# for i in sorted(dct.keys()):
#     k = dct[i]
#     print(k[0])

# def fun(x):
#     global y
#     y = x * x
#     return y
# fun(2)
# print(y)

# def f(x):
#     if x == 0:
#         return 0
#     return x + f(x - 1)
# print(f(3))

# tupla = ('1', '2', '3')
# print(tupla[1:2])
# del tupla[1]

# def function(x=0):
#     return x
# print(function(1))

# def func(a, b):
#     return a * b
# print(func(2))

# dct = {'one':'two', 'three':'one', 'two': 'three'}
# v = dct['one']
# print(v)
# for k in range(len(dct)):
#     v = dct[v]
# print(v)

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return
# print(fun(fun(2)) + 1)

# def fun(x, y, z):
#     return x + 2 * y + 3 * z
# print((fun(0, z=1, y=3)))

# def fun(x):
#     x += 1
#     return x
# x = 2
# x = fun(x + 1)
# print(x)

# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)
#
# in_ = 2

def checkio(words: str) -> bool:
    cont = 0
    for i in words.split():
        if i.isalpha():
            cont +=1
        else:
            cont +=0
        if cont == 3:
            return True
    return False
