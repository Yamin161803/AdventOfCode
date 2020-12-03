with open("Day_3.txt", "r") as item:

    file = item.read().split("\n")


data = []
for item in file:
   data.append(list(item))
x=0
answer = 0
for item in range(0,len(data),2):

    if  data[item][x%31] == "#":
        answer +=1

    x+=1

print(answer)
print(63*181*55*67*30)
