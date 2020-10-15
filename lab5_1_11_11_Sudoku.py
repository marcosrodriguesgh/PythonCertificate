def validentry(lista):
    return True if ''.join(sorted(lista)) == '123456789' else False


entry = ('295743861', '431865927', '876192543', '387459216', '612387495', '549216738', '763524189', '928671354',
         '154938672')
entry = ('195743862', '431865927', '876192543', '387459216', '612387495', '549216738', '763524189', '928671354',
         '254938671')
entrylist = []
entryfliped = [[] for _ in range(9)]
entry3x3 = []
for i, e in enumerate(entry):
    temp = []
    for j, x in enumerate(e):
        temp.append(x)
        entryfliped[j].append(x)
    entrylist.append(temp)

for q in range(0, 9, 3):
    temp = []
    for li, l in enumerate(entrylist):
        temp += l[q:q+3]
        if li % 3 == 2:
            entry3x3.append(temp)
            temp = []

for x, y, z in zip(entrylist, entryfliped, entry3x3):
    if validentry(x) and validentry(y) and validentry(z):
        output = 'Yes'
    else:
        output = 'No'
        break
print(output)



