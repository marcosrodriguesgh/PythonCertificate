lista = [24, 1, 2, 78, 5, 3, 8, 21, 9, 0, 4, 23, 67, 98, 456]
tamanho = len(lista)-1
count = 0
while count < len(lista):
    #count = 0
    for i in range(0, tamanho):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            print(lista)
    tamanho -= 1
    count += 1
print(lista)

print('='*50)#=================================

myList = [8, 10, 6, 2, 4]
houveswap = True
while houveswap:
    houveswap = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            myList[i], myList[i + 1] = myList[i + 1], myList[i]
            houveswap = True
print(myList)