message = input('Write an message to bem encrypted: ')
encrypted_msg = ''
for c in message:
    if not c.isalpha():
        continue
    c = c.upper()
    code = ord(c)
    code += 1
    if code > ord('Z'):
        code = ord('A')
    encrypted_msg += chr(code)
print(encrypted_msg)
