pattern = ('###', '# #', '  #', '#  ')
def generate_numbers():
    padrao = ('  # ### ### # # ### ### ### ### ### ###',
              '  #   #   # # # #   #     # # # # # # #',
              '  # ### ### ### ### ###   # ### ### # #',
              '  # #     #   #   # # #   # # #   # # #',
              '  # ### ###   # ### ###   # ### ### ###')
    numeros = [[], [], [], [], [], [], [], [], [], []]
    for e in padrao:
        i = 0
        for c in range(0, 10):
            numeros[c].append(pattern.index(e[i:i + 3]))
            i += 4
    return numeros

numeros_map = generate_numbers()

num = '1234567890'
for i in range(5):
    for n in num:
        print(pattern[numeros_map[int(n)-1][i]], ' ', end='')
    print()
