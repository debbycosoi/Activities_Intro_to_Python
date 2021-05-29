# Write a function that does what the List.max() method does.
# Your function will given a list of numbers as a parameter and you are to return the greatest
# value in that list without using the List.max() method.

def maxVal(myList):
    length = len(myList)
    for i in range(0,length):
        maxValIndex = i
        for j in range(i+1, length):
            if (myList[j] > myList[maxValIndex]):
                maxValIndex = j
    print(myList[maxValIndex])


myList = [7,3,99,35,34,204,999, 38394839]
print(f"The max value of the list is:")
maxVal(myList)