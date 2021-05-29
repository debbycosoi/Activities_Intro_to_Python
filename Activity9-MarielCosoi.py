# Write a function that given a list will print out all the values in that list
# Write a function that takes in one integer as a parameter and will print out your name as many
# times as specified by the argument.

myList = ["Elvis", "Travis", "Alexa", "HelloGoogle"]
myList2 = ["bibidi", "babidi", "boo"]
def first(myList = myList):
    for i in myList:
        print(i)

manyTimes = 10


def second(manyTimes):
    myName = "Debby"
    for j in range(1,manyTimes):
        print(myName)

first(myList2)
second(20)