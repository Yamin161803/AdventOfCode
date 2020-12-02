from os import spawnl


with open("2020/Day_2.txt", "r") as item:

    file = item.read().split("\n")
data = []
for item in range(len(file)):
    data.append(file[item].split(":"))


answer = 0

for item in data:
    temp = item[0].split(" ")
    förstIndex, secondeIndex = map(int, temp[0].split("-"))
    alfabetet = temp[1]
    string = list(item[1])

    if ((string[förstIndex] == alfabetet) or (string[secondeIndex] == alfabetet)) & (
        string[förstIndex] != string[secondeIndex]
    ):
        answer += 1

    """count = 0
    for char in range(1, len(string)):
        if string[char] == alfabetet:
            count += 1
    if (count >= minNumber) & (count <= maxNumber):
        print(item)
        answer += 1
    """
print(answer)