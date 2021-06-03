def cubed (x):
    return x**3

cubed = lambda x : x**8

example = [2,3,4,5,6]

cubed2 = list(map(lambda x : x**3, example))

print(cubed2)

#1. Write a Python program to triple all numbers of a given list of integers. Use Python map.

triple = list(map(lambda x : x*3, example))

print(triple)

#2. Write a Python program to add three given lists using Python map and lambda.

myList1 = [1,2,3]
myList2= [4,5,6]
myList3= [7,8,9]

addThree = list(map(lambda a,b,c : a+b+c, myList1,myList2,myList3))

print(addThree)

#3. Write a Python program to listify the list of given strings individually using Python map.

myList4 = ["Elvis", "Tyler", "Code"]

listify = list(map(list, myList4))

print(listify)