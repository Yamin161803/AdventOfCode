import re


def dayThree(fileName):
    with open(fileName, "r") as item:
        file = item.read().split("\n\n")

    answer = 0
    for item in file:
        color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        requirements = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        temp = re.split("\n| ", item)
        for secondItem in temp:
            remove = False
            array = secondItem.split(':')
            if array[0] == "byr":
                if (int(array[1]) <= 2002) & (int(array[1]) >= 1920):
                    remove = True
            if array[0] == "iyr":
                if (int(array[1]) >= 2010) & (int(array[1]) <= 2020):
                    remove = True
            if array[0] == "eyr":
                if (int(array[1]) >= 2020) & (int(array[1]) <= 2030):
                    remove = True
            if array[0] == "hgt":
                if (array[1][-2:] == 'cm') or (array[1][-2:] == 'in'):
                    if (array[1][-2:] == 'cm') & (int(array[1][:-2]) >= 150) & (int(array[1][:-2]) <= 193):
                        remove = True
                    if (array[1][-2:] == 'in') & (int(array[1][:-2]) >= 59) & (int(array[1][:-2]) <= 76):
                        remove = True

            if array[0] == "hcl":
                if (array[1][:1] == "#") & (len(array[1]) == 7) & (
                        not bool(re.compile(r'[^a-z0-9.]').search(array[1][1:]))):
                    remove = True
            if array[0] == "ecl":
                if array[1] in color:
                    remove = True
            if array[0] == "pid":
                if len(array[1]) == 9:
                    remove = True
            if remove:
                requirements.remove(array[0])
        if not requirements:
            answer += 1
    return answer


print(dayThree("Day_4.txt"))
