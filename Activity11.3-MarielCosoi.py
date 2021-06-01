# #Activity 11.3: 
# '''
# 1. Create a function that given a list of numbers, will return to me a list of booleans
# 2. Your function will take in a list of numbers, and if the values are less than 55 exclusive, then you substitute that list item with a "False". For all others, substitute the current list item value to "True". 
# 3. Return to me that list, and before returning check its type (It should a list... )


def isBool(myList = [3,66,43,12,44]):
    length = len(myList)
    for i in range (0, length):
        if (myList[i] < 55):
            myList[i] = False
        else:
            myList[i] = True
    print(type(myList))
    print(myList)

myList = [3,66,43,12,44, 99, 100]
isBool(myList)
