with open("2020/Day_1.txt", "r") as item:
    data = item.read().split("\n")


array = []
run = True
answere = 0
for item in range(len(data)):
    if not run:
        break
    for secondItem in range(item, len(data)):
        if not run:
            break
        for thirdItem in range(secondItem, len(data)):
            if int(data[item]) + int(data[secondItem]) + int(data[thirdItem]) == 2020:
                array.append(int(data[item]))
                array.append(int(data[secondItem]))
                array.append(int(data[thirdItem]))
                answere = int(data[item]) * int(data[secondItem]) * int(data[thirdItem])
                run = False
            if not run:
                break
print(array)
print(sum(array))
print(answere)
