from random import randint
temps = [[randint(0, 1000) for h in range(24)] for d in range(31)]
#matrix[0][0] = 24.7
print(temps)

noon = 0.0
for day in temps:
    noon += day[11]
print(noon / 31)


maxtemp = 0
for day in temps:
    if max(day) > maxtemp:
        maxtemp = max(day)
print(maxtemp)


maxtemp = 0
for day in temps:
    for hour in day:
        if hour > maxtemp:
            maxtemp = hour
print(maxtemp)

more20 = 0
for day in temps:
    if day[11] >= 20:
        more20 += 1
print(more20)
