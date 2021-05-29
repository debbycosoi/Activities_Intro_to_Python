# num = 5
# while(num == 5):
#    print("well Done")

# sum = 0
# i =1
# while(i < 10):
#     sum = sum + i 
#     i = i+ 1

# print(sum)

#Mini Activity

# 2. Create a While loop that takes a list of integers, and gives the sum of the integers.

print("1. Create a While loop that goes through the 12 days of Christmas:")
day = 1
index = 0
gift = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]

while (day < 13):
    day = day +1
    index = index +1
    print(f"On the {day-1} day/s of Christamas my true love gave me {gift[index-1]}")

print("2. Create a While loop that takes a list of integers, and gives the sum of the integers.")
myList = [1, 2, 3, 4, 5, 6]
sum = 0
i = 0
lenght = len(myList)

while (i < lenght ):
    sum = sum + myList[i]
    i = i+1

print(f"the sum of integers of my list is {sum}")

print("Repeat excercise 1. using For Loops")
for day2 in range(1,13):
     print(f"On the {day2} of Christamas my true love gave me {gift[day2-1]}")
