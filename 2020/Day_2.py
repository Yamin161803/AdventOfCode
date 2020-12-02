from os import spawnl


def dayTwo(file):
    data = []
    for item in range(len(file)):
        data.append(file[item].split(":"))

    answer = 0

    for item in data:
        temp = item[0].split(" ")
        minNumber, maxNumber = map(int, temp[0].split("-"))
        alfabetet = temp[1]
        string = list(item[1])

        # Detta if stats för andra tjärnan
        if ((string[minNumber] == alfabetet) or (string[maxNumber] == alfabetet)) & (
            string[minNumber] != string[maxNumber]
        ):
            answer += 1

        # detta för första tjärnan
        """count = 0
        for char in range(1, len(string)):
            if string[char] == alfabetet:
                count += 1
        if (count >= minNumber) & (count <= maxNumber):
            print(item)
            answer += 1
        """
    return answer


with open("2020/Day_2.txt", "r") as item:

    file = item.read().split("\n")


print(dayTwo(file))