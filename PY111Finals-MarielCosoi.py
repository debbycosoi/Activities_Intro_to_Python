# Coding Challenges

# Given two int values, return their sum. Unless the two values are the same, then return the square their sum.


# sum_squared(1, 2) → 3
# sum_squared(3, 2) → 5
# sum_squared(2, 2) → 16

print("Question 16:")
def sum_squared(a,b):
    if(a==b):
        return (a+b)*(a+b)
    else:
        return (a+b)

print("Example for question 16:")
print(sum_squared(2, 2))

# Using List Comprehension, write a function that given a list of numeric values will generate and return a new list of values with each item in the original list cubed (raised to the third power)


# Input: [0, 1, 2, 4] 
# Output: [0, 1, 8, 64]

print("Question 17:")
inputList = [0, 1, 2, 4] 
def power():
    [x**3 for x in inputList]

print("Output for question 17:")
print(inputList)

# Given an int array length 2, return True if it contains a 2 or a 3.


# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False

print("Question 18:")
def has23(c,d):
    li = [c,d]
    if ((c==2) or (c==3) or (d==2) or (d==3)):
        return True
    else:
        return False

print("Example for question 18:")
print(has23(4,3))

# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

print("Question 19:")
def count_evens(nums):
    count = 0
    for i in range(len(nums)):
        if (nums[i] % 2 == 0):
            count = count + 1
    return count

print("Example for question 19:")
nums = [2, 1, 2, 3, 4]
print(count_evens(nums))

# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.


# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

print("Question 20:")
def lucky_sum(a,b,c):
    if (a == 13):
        return 0
    if (b == 13):
        return a
    if (c == 13):
        return a+b
    if (a!=13 and b!=13 and c!=13):  
        return (a+b+c) 

print("Example for question 20:")
print(lucky_sum(1, 13, 3))