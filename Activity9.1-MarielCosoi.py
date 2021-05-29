# Create a function that is given a list of numbers as a parameter.
# Sort this list in any way other than using methods from the List object. 

def sortList(myOldList):
    myList = myOldList.copy()
    length = len(myList)
    for i in range(0,length):
        minIndex = i
        for j in range (i+1, length):
            if(myList[j] < myList[minIndex]):
                minIndex = j
            mid = myList[i] 
            myList[i] = myList[minIndex]
            myList[minIndex] = mid
    return myList

myList = [44,22,4]
print("My old list")
print(myList)
print("My sorted list")
print(sortList(myList))

