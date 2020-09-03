def isYearLeap(year):
    if year % 400 == 0:
        pass
    elif year % 4 == 0 and year % 100 != 0:
        pass
    else:
        print('não é bi -> ', end='')
        return False
    return True

def daysInMonth(year, month):
    months30 = (4, 6, 9, 11)
    months31 = (1, 3, 5, 7, 8, 10, 12)
    if month in months30:
        return 30
    elif month in months31:
        return 31
    elif int(month) == 2 and isYearLeap(year):
        return 29
    else:
        return 28

def dayOfYear(year, month, day):
    count = 0
    if month == 1:
        pass
    else:
        for i in range (1, month):
            count += daysInMonth(year, i)
    return count + day

print(dayOfYear(2017, 1, 30))