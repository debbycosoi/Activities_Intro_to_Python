import math

# Write a function that will be passed a String as a parameter
# Your functions job is determine whether or not the String passed in is a Palindrome

def isPalindrome(stg):
    strip = stg.strip()
    low = strip.lower()
    length = len(low)
    half = math.ceil(length/2)
    for i in range (0,half):
        if low[i] != low[-(i+1)]:
            return False
    return True

stg = "rac e caR"
stg2 = "Elvis"
stg3 = ""
solution = isPalindrome(stg3)
print(solution)
print(stg3)
