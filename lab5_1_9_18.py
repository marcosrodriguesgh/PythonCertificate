def mysplit(strng):
    strng = strng.strip()
    output = []
    word = ''
    if strng:
        for i in strng:
            if i == ' ':
                output.append(word)
                word = ''
            else:
                word += i
        output.append(word)
        return output
    return []

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))