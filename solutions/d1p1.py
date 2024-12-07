file = open("d1_input.txt", "r")

listOne = []
listTwo = []
sortOne = []
sortTwo = []

distanceTotal = 0
simScore = 0
simCount = 0
comp = 0
index = 0

for x in file:
    listOne.append(x[0:5])
    listTwo.append(x[8:13])

listOne.sort()
listTwo.sort()
sortOne = [int(x) for x in listOne]
sortTwo = [int(x) for x in listTwo]

for x in sortOne:
    if x > sortTwo[index]:
        comp = x - sortTwo[index]
    else:
        comp = sortTwo[index] - x
    distanceTotal += comp
    index += 1

maxIndex = index
index = 0

for x in sortOne:
    simCount = sortTwo.count(x)
    simScore += x * simCount
    simCount = 0
    index = 0

print("Total Distance: " + str(distanceTotal))
print("Similarity Score: " +  str(simScore))
