
def DaySixFirst(fileName):
    with open(fileName, "r") as item:
        file = item.read().split("\n\n")

    questionAnswered = []

    for item in file:
        temp = set(item)
        if '\n' in temp:
            temp.remove('\n')

        questionAnswered.append(len(temp))

    print(questionAnswered)

    return (sum(questionAnswered))

def DaySix(fileName):
    with open(fileName, "r") as item:
        file = item.read().split("\n\n")

    questionAnswered = []

    for item in file:
        tempgroup =item.split('\n')

        questionAllAnswered={}
        print(tempgroup)
        for Id in range(len(tempgroup)):
            if Id==0:
                questionAllAnswered = set(tempgroup[Id])
            elif len(tempgroup[Id])==0:
                break
            else:
                questionAllAnswered = questionAllAnswered.intersection(set(tempgroup[Id]))
        questionAnswered.append(len(questionAllAnswered))

    return sum(questionAnswered)

print(DaySix("Day_6.txt"))