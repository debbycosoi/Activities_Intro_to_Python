# Write a function called isSorted which will be passed in a list of numbers
# Your functions job is to determine if the list is in need of being sorted, or if it already came sorted.
# Your function should return a boolean determining whether or not that is the case.

def isSorted(myList):
    myOldList = myList.copy()
    length = len(myList)
    for i in range(0,length):
        minIndex = i
        for j in range (i+1, length):
            if(myList[j] < myList[minIndex]):
                minIndex = j
        if (minIndex != i):
            mid = myList[i] 
            myList[i] = myList[minIndex]
            myList[minIndex] = mid
    if (myOldList == myList):
        return True
    else:
        return False


myList = [1,6,5,7,8,4332,2,3]
myList2 = [1,2,3,4,5]
isSorted(myList2)

def isSorted2(myList):
    length = len(myList)
    for i in range(0, length-1):
        if (myList[i] > myList[i+1]):
            return False
    return True

solution = isSorted2(myList2)
print(solution)