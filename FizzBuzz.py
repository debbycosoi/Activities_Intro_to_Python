# print values from 1-100. If the number is divisible by 3, print "fizz" if the number is divisible by 3 and 5 print "fizzbuzz"


def fizzbuzz():
    for i in range(1,101):
        if(i % 3 == 0 and i% 5 == 0):
            print ("FizzBuzz")
        elif(i % 3 == 0):
            print ("Fizz")
        elif(i % 5 == 0):
            print ("Buzz")
        else: 
            print (i)

fizzbuzz()


