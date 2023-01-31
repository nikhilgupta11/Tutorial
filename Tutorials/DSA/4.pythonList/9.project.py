from numpy import average


numOfDays = int(input("Enter number of days?"))
temp = []
for i in range(numOfDays):
    day = int(input("Day" + str(i+1) + "high tempreture:"))
    temp.append(day)
average = sum(temp)/len(temp)
print(average)

count = 0
for i in temp:
    if i > average:
        count = count + 1
print(str(count) + "days are above")
