def dayThree(increaseRightBy, increaseDownBy, fileName):
    with open(fileName, "r") as item:
        file = item.read().split("\n")
    answer = 0
    x = 0
    for item in range(0, len(file), increaseDownBy):

        temp = list(file[item])
        if temp[x % len(temp)] == "#":
            answer += 1
        x += increaseRightBy
    return answer

test = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

answer = 1
for y in test:
    answer*=dayThree(y[0], y[1], "Day_3.txt")
print(answer)

