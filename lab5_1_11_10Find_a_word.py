def find_word(exp, word):
    i = 0
    for x in word:
        if exp[i:].find(x) == -1:
            return 'No'
        else:
            i = exp[i:].find(x)
    return 'Yes'


print(find_word('Nabucodonosor', 'donor'))
print(find_word('Nabucodonosor', 'donut'))
