def isPrime(num):
    retorno = False
    primos = [2]
    for dividendo in range(3, num + 1):
        # print(f'\ndividendo={dividendo}; ', end='')
        for divisor in primos:
            # print(f'divisor ={divisor}; ', end='')
            if dividendo % divisor == 0:
                retorno = False
                break #return False
            else:
                if dividendo // divisor < divisor:
                    primos.append(dividendo)
                    retorno = True
                    break
    # print()
    # print(primos)
    return retorno
for i in range(1, 100):
	if isPrime(i + 1):
	    print(i + 1, end=" ")
print()
