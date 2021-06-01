import statistics
import random

#Activity 11 and 11.2

def examGrades(grades):
    dev = statistics.stdev(grades)
    newGrades = []
    for i in range(len(grades)):
        newGrade = grades[i] + dev
        if (newGrade <= 100):
            newGrades.append(newGrade)
        else:
            newGrades.append(100)
    return newGrades


def ranList (num):
    listOfGrades = []
    for i in range(num):
        ranGrade = random.randrange(0,101)
        listOfGrades.append(ranGrade)
    return listOfGrades


num = 5
grades = ranList(num)
print("The original grades are:")
print(grades)
print("The new grades are:")
print(examGrades(grades))

def av():
    ex = examGrades(grades)
    average = statistics.mean(ex)
    print (f"The average is {average}")

av()


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

# '''
# Now I would like to have a function that takes a list and tells me how many people passed the class
# I would like you to do this with a given list of "grades"
# Given a list of integers representing exam grades (Whether they are curved or not), print a message telling me how many people passed or failed the class based on the fact that 55+ is passing and below is failing.
# Call this function "Class Report".


def classReport(myList = [3,66,43,12,44]):
    length = len(myList)
    for i in range (0, length):
        if (myList[i] < 55):
            myList[i] = False
        else:
            myList[i] = True
    print(type(myList))
    print(myList)
    passStudents = myList.count(True)
    failStudents = myList.count(False)
    sentence = f"Of the Class of {length}, {passStudents} passed and {failStudents} failed"
    print(sentence)

myList = [3,66,43,12,44, 99, 100]
classReport(myList)

