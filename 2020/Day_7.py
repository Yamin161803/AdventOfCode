import re



def DaySeven(fileName):
    with open(fileName, "r") as item:
        file = item.read().split("\n")

    data=[]
    scr=[]
    bagsNeeded=['shiny gold']
    run = True
    firsTime=True
    for item in file:
        item = item[:-1].replace(" bags", "").replace(" bag", "")
        data.append(re.split(" contain [1-9] | contain |, [1-9] ", item))

    while run:
        bagsNeeded=[]
        if firsTime:
            bagsNeeded = ['shiny gold']
            firsTime = False
        else:
            for item in temp:
                if item not in scr:
                    bagsNeeded.append(item)
                    scr.append(item)
        run = False
        temp=[]
        for groupBags in data:
            for bags in range(1,len(groupBags)):
                for bagsCheck in bagsNeeded:
                    if (bagsCheck == groupBags[bags]) :
                        run = True
                        temp.append(groupBags[0])
    print(len(set(scr)))




DaySeven("Day_7.txt")