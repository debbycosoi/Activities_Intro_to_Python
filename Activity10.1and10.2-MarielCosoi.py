#Write a function that will take an integer as a parameter, and will create a list of the size passed in as an argument, and will populate the list with a random number between 0-1023 (inclusive). You're going to be using "getrandbits()" method so think about how to arrive at that outcome.
import random

def ranNum (num):
    myList = []
    for i in range (0, num):
        myList.append(random.getrandbits(10))
    return myList

num = 4
print(ranNum(num))

#Problem: Let's say that we want to generate a random number, but we don't want to represent the range by the amount of bits, but explicitly with a range and using decimal number.
#Using ".randrange(x,y)"

#Activity 10.2:
#Similar to the previous problem, create a function that creates a random list with numbers from 20-40 (excliuding 40)

def ranNum2 (num):
    myList = []
    for i in range (0,num):
        ranNumOfMyList = random.randrange(20,40)
        myList.append(ranNumOfMyList)
    return myList

num2 = 5
solution = ranNum2(num2)
print(solution)