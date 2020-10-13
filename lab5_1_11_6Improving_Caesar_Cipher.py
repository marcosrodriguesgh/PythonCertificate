msg = ''
shift = ''
newmsg = ''
while not msg:
    msg = input('Please write your message: ')
while not shift.isnumeric():
    shift = input('Please, enter the number to shift: ')
for c in msg:
    if c.isalpha():
        newc = ord(c.lower()) + int(shift)
        if newc > 122:
            newc = (newc % 122) + 96
        newmsg += chr(newc).upper() if c.isupper() else chr(newc)
    else:
        newmsg += c
print(newmsg)
