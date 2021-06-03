
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

def sleep_in(weekday, vacation):
  return True if not weekday or vacation else False



# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.


# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False


def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile:
    return True
  else:
    return False

a_smile = True
a_smile = False

monkey_trouble

monkey_troubule2 = lambda s_smile,b_smile: True if a_smile == b_smile else False

def monkey_trouble3(a_smile, b_smile):
  return a_smile == b_smile


# Given two int values, return their sum. Unless the two values are the same, then return double their sum.


# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

sum_double = lambda a,b : 2*a+2*b if a==b else a+b

# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.


# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0

diff21 = lambda n: abs(n-21) if n<21 else abs(2*(n-21))


# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False

def parrot_trouble(talking, hour):
    if (7 <= hour <= 20):
      return False
    else:
      if (talking == True):
        return True
      else:
        return False

parrot_trouble = lambda talking, hour : False if 7 <= hour <= 20 else True if talking == True else False


# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True

def makes10(a, b):
  if(a== 10 or b ==10 or a+b==10):
    return True
  else:
    return False

makes10_1 = lambda a,b : True if a== 10 or b ==10 or a+b==10 else False


# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False

def near_hundred(n):
  if (abs(100-n) <= 10) or (abs(200-n) <= 10):
    return True
  else:
    return False


# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-4, -5, True) → True

def pos_neg(a, b, negative):
  if (negative == True):
    if (a < 0 and b < 0):
      return True
    else:
      return False
  elif (a > 0 and b < 0) or (a < 0 and b > 0) :
    return True
  else:
    return False

# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'

def not_string(str):
  myStrList = list(str)
  myListNot = ["n","o","t"]
  if (len(myStrList) < 3):
    return "not "+str
  else:
    for i in range (0,4):
      if (myStrList[i] != myListNot[i]):
        return "not "+str
      else:
        return str
