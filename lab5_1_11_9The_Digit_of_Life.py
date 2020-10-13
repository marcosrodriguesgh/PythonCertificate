def digit_of_live(dateofbirth):
    output = 0
    for x in dateofbirth:
        output += int(x)
    return digit_of_live(str(output)) if output >= 10 else output


date = input('Please, give you birthday (YYYYMMDD): ')
print(digit_of_live(date))
