a=3
b=4
c=1

myList = [a, b, c]

def mySort(myList):
    maxNum = max(myList)
    minNum = min(myList)
    if(myList[0] != maxNum and myList[0] != minNum):
        return (minNum, myList[0], maxNum)
    elif(myList[1] != maxNum and myList[1] != minNum):
        return (minNum, myList[1], maxNum)
    else:
        return (minNum, myList[2], maxNum)

print(f"I have a list called myList: {myList}, if I order it and turn it into a tuple i get:")
print(mySort(myList))

print("The type of my anwer is:")
print(type(mySort(myList)))

print("Another way of doing the same gives me the ordered tuple:")
def secondChance(myList):
    maxNum = max(myList)
    minNum = min(myList)
    indexMax = myList.index(maxNum)
    indexMin = myList.index(minNum)
    myList.remove(maxNum)
    myList.remove(minNum)
    return (minNum, myList[0], maxNum)

print(secondChance(myList))
