import re
with open("Day_4.txt", "r") as item:
    file = item.read().split("\n\n")



answer=0
for item  in file:
    temp = []
    correct = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    temp=(re.split('\n| ',item))
    print(temp)
    
    for value in temp:
        print(value[:3])
        if value[:3] in correct:
            correct.remove(value[:3])


    if not correct:
        answer+=1

print(answer)