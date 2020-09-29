try:
    x = int(input('Enter a number: '))
    y = 1/x
    print(y)
except ZeroDivisionError:
    print('Divisão por zero')
except ValueError:
    print('Valor inválido, informe um inteiro')
