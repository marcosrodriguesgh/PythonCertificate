def readint(prompt, min, max):
    try:
        num = int(input(prompt))
        if num < min or num > max:
            raise BaseException
        return num
    except ValueError:
        print('Error: wrong input')
        return readint(prompt, min, max)
    except BaseException:
        print(f'Error: the value is not within permitted range ({min}..{max})')
        return readint(prompt, min, max)

v = readint("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
