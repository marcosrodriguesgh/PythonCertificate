# Item 1
print('Item 1')
vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]
print(vals)

# Item 2 - errei
print('Item 2')
nums = [1, 2, 3]
vals = nums[-1:-2]
print(vals)

# Item 3
print('Item 3')
lst = [3, 1, -2]
print(lst[lst[-1]])

# Item 4
print('Item 4')
for i in range(1):
    print('#')
else:
    print('#')

# Item 5
print('Item 5')
x = 1
x = x == x
print(x)

# Item 6 - errei
print('Item 6')
vals = [0, 1, 2]
vals.insert(0, 1)
print(vals)
del vals[1]
print(vals)

# Item 7 - errei
print('Item 7')
a = 1
b = 0
c = a & b
print('c: ',c)
d = a | b
print('d: ', d)
e = a ^ b
print('e: ', e)
print(c + d + e)

# Item 8
print('Item 8')
ls1 = [1, 2, 3]
ls2 = []
for v in ls1:
    ls2.insert(0, v)
print(ls2)

# Item 9
print('Item 9')
t = [[3-i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)

# Item 11 - errei
print('Item 11')
i = 0
while i <= 3:
    i += 2
    print('*')

# Item 12
print('Item 12')
lst = [i for i in range(-1, 2)]
print(lst)

# Item 13
print('Item 13')
var = 1
while var < 10:
    print('#',var)
    var = var << 1

# Item 14 - errei
print('Item 14')
lst = [[0, 1, 2, 3] for i in range(2)]
#print(lst[2][0])

# Item 15
print('Item 15')
nums = [1, 2, 3]
vals = nums
del vals[1:2]
print(nums)
print(vals)

# Item 16
print('Item 16')
z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

# Item 17
print('Item 17')
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print('#')

# Item 18
print('Item 18')
lst = [1, 2, 3]
for v in range(len(lst)):
    lst.insert(1, lst[v])
print(lst)

# Item 19
print('Item 19')
i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print('*')

# Item 20
print('Item 20')
lst = [1, 2, 3, 4]
print(lst[-3: -2])

