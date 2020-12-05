def dayFive(fileName):
    with open(fileName, "r") as item:
        data = item.read().split("\n")

    answer=[]
    for item in data:
        availableSetsRemaining=128
        seatNumber=127
        columns=7
        availableColumnsRemaining = 8
        for value in range(len(item)):
            if value <=6:
                availableSetsRemaining /= 2
                if item[value]=="F":
                    seatNumber-=availableSetsRemaining
            else:
                availableColumnsRemaining/=2
                if item[value]=="L":
                    columns -= availableColumnsRemaining
        answer.append(int(seatNumber*8 + columns))
    #Andra tjärnan
    for number in range(96,911):
        if number not in answer:
            return number
    #första tjärnan
    return max(answer)


print(dayFive("Day_5.txt"))