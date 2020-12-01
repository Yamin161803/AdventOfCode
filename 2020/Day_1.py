with open("2020/Day_1.txt", "r") as item:
    data = item.read().split("\n")


array = []
run = True
answere = 0
for item in range(len(data)):
    if not run:
        break
    for secondItem in range(len(data)):
        if (int(data[item]) + int(data[secondItem]) == 2020) & (item != secondItem):
            array.append(data[item])
            array.append(data[secondItem])
            answere = int(data[item]) * int(data[secondItem])
            run = False
        if not run:
            break
print(array)
print(1184 + 836)
print(answere)
