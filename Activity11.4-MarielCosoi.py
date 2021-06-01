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
