def dayOne(data: list):
    array = []
    answer = 0
    for item in range(len(data)):

        for secondItem in range(item, len(data)):

            for thirdItem in range(secondItem, len(data)):
                if (
                    int(data[item]) + int(data[secondItem]) + int(data[thirdItem])
                    == 2020
                ):
                    array.append(int(data[item]))
                    array.append(int(data[secondItem]))
                    array.append(int(data[thirdItem]))
                    answer = (
                        int(data[item]) * int(data[secondItem]) * int(data[thirdItem])
                    )

    print(array)
    print(sum(array))
    return answer


with open("2020/Day_1.txt", "r") as item:
    data = item.read().split("\n")


print(dayOne(data))