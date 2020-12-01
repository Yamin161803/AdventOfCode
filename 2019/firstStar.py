import math

with open("input.txt", "r") as item:
    data = item.read().split("\n")

summa = 0


for item in data:
    sub = []
    temp = math.floor(int(item) / 3) - 2
    while temp > 0:
        sub.append(temp)
        temp = math.floor(temp / 3) - 2
    summa += sum(sub)

print(summa)