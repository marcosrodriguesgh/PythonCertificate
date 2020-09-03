def isYearLeap(year):
    if year % 400 == 0:
        print('é bi -> ', end='')
    elif year % 4 == 0 and year % 100 != 0:
        print('é bi -> ', end='')
    else:
        print('não é bi -> ', end='')
        return False
    return True


def daysInMonth(year, month):
    months30 = (4, 6, 9, 11)
    months31 = (1, 3, 5, 7, 8, 10, 12)

    if month in months30:
        print(30)
        return 30
    elif month in months31:
        print(31)
        return 31
    elif int(month) == 2 and isYearLeap(year):
        print(29)
        return 29
    else:
        print(28)
        return 28


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")