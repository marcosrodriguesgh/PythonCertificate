msg = 'Ten animals I slam in a net'
msg = ''
tup = [x.lower() for x in msg.strip() if x != ' ']
reverse = list(reversed(tup))
if tup and tup == reverse:
    print('É palindromo')
else:
    print('It is not palindrome')