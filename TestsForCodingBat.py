# def max_end3(nums):
#     length = len(nums)
#     newList = []
#     first = nums[0]
#     last = nums[-1]
#     if (first > last):
#         for i in range (0,length):
#             newList = newList.append(first)
#     else:
# #         for i in range (0,length):
# # #             newList = newList.append(last)
# # #     return newList


# # # nums = [1,2,3,4]
# # # print(max_end3(nums))

# # def sum67(nums):
# #   sum = 0
# #   for i in range (len(nums)):
# #     if 

# # def sum13(nums):
# #   sum = 0
# #   for i in range (len(nums)):
# #     if (nums[i] != 13):
# #       if (i == 0 or nums[i-1] != 13):
# #         sum = sum + nums[i]
# #   return sum
  

# def fix_teen(n):
#   if (13>= n >=19):
#     if (n != 15 or n != 16):
#       return 0
#     elif (n == 15):
#       return 15
#     else:
#       return 16
#   else:
#     return n
  
# def no_teen_sum(a, b, c):
#   return fix_teen(a)+fix_teen(b)+fix_teen(c)

# a= 2
# b=13
# c=1
# print(no_teen_sum(a, b, c))

# def close_far(a, b, c):
#   if (abs(a-b) <= 1) or(abs(a-c) <= 1) and 
    

# def make_bricks(small, big, goal):
#   smallBricks = []
#   bigBricks = []
#   sumBricks = 0
#   for i in range (0, small):
#     smallBricks.append(1)
#   for i in range (0,big):
#     bigBricks.append(5)
#   totalList = bigBricks + smallBricks
#   if (sum(totalList) == goal):
#     return True
#   elif (sum(totalList < goal):
#     return False
#   elif (sum(smallBricks) == goal):
#     return True
#   elif (sum(bigBricks) == goal):
#     return True
#   else:
#     return False
#   for i in range (0,len(totalList)):
#     sumBricks = sumBricks + totalList[i]
#     if (sumBricks == goal):
#       return True
#     elif (sumBricks > goal):
#       return False
#     else:
#       return False

# tests = [
# [3, 1, 8],
# [3, 1, 9],
# [3, 2, 10],
# [3, 2, 8],
# [3, 2, 9],
# [6, 1, 11],
# [6, 0, 11],
# [1, 4, 11],
# [0, 3, 10],
# [1, 4, 12],
# [3, 1, 7],
# [1, 1, 7],
# [2, 1, 7],
# [7, 1, 11],
# [7, 1, 8],
# [7, 1, 13],
# [43, 1, 46],
# [40, 1, 46],
# [40, 2, 47],
# [40, 2, 50],
# [40, 2, 52],
# [22, 2, 33],
# [0, 2, 10],
# [1000000, 1000, 1000100],
# [2, 1000000, 100003],
# [20, 0, 19],
# [20, 0, 21],
# [20, 4, 51],
# [20, 4, 39]
# ]

# def make_bricks(small, big, goal):
#   result = 0
#   if ((small + big*5) < goal):
#     return False
#   while(small >= 0):
#     if((goal-result) % 5 == 0 and (goal-result)/5 <= big):
#       return True
#     else:
#       result = result + 1
#       small = small - 1
#   return False

# for test in tests:
#   print(make_bricks(test[0],test[1],test[2])) 


# 2

# def front_back(str):
#   if (len(str) == 1):
#     return str
#   else:
#     result = str[-1]+str[1:len(str)-1] + str[0]
#   return result

# lala = "hola"

# print(front_back(lala))

# def last2(str): 
#   sum = 0
#   end = (str[-2]+str[-1])
#   for i in range (0,len(str)-2):
#     if ((str[i]+str[i+1]) == end ):
#       sum = sum + 1
#   return sum
    
# print(last2("axxxaaxx"))

# def array_front9(nums):
#   minNum = min(len(nums), 4)
#   print(minNum)
#   for i in range (0, minNum):
#     if (nums[i] == 9):
#       return True
#   return False

# nums = [1, 2, 9, 3, 4]
# print(array_front9(nums))

# nums = [1, 1, 2, 3, 1]
# newList = [nums[0],nums[1],nums[2]]
# print(newList)


# def count_hi(str):
#   sum = 0
#   str1 = str.lower()
#   if (len(str1) <=2):
#     if (str1 == "hi"):
#       sum = 1
#     else:
#       sum = 0
#   if (str1[-2]+str1[-1] == "hi"):
#     sum =1
#   for i in range (0, len(str)-2):
#     if ((str1[i] + str1[i+1]) == "hi"):
#       sum = sum + 1
#   return sum
    


# def cat_dog(str):
#   cat = 0
#   dog = 0
#   if (len(str) <=3):
#     if (str == "cat"):
#       cat = 1
#     elif (str == "dog"):
#       dog = 1
#     print(cat)
#     print(dog)
#   for i in range(0,len(str)-3):
#     if ((str[i] + str[i+1] + str[i+2]) == "cat"):
#       cat = cat + 1
#       print(cat)
#     for i in range(0,len(str)-3):
#       if ((str[i] + str[i+1] + str[i+2]) == "dog"):
#         dog = dog + 1
#         print(dog)
#   if (cat == dog):
#     return True
#   else:
#     return False

# cat_dog("stcatdog")

# def string_match(a, b):
#   count = 0
#   shorter = min(len(a), len(b))
#   for i in range(0,(shorter-1)):
#     a_sub = a[i:i+2]
#     b_sub = b[i:i+2]
#     if a_sub == b_sub:
#       count = count + 1
#   return count

def count_code(str):
  count = 0
  if (len(str)<=4):
    if ((str[0:2] == "co") and (str[3] == "e")):
      return 1
    else:
      return 0
  for i in range (len(str)):
    if ((str[i:i+2] == "co") and (str[i+3] == "e")):
      count = count + 1
  return count
      
str = "cozexxcope"

print(count_code(str))