import statistics
import random

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