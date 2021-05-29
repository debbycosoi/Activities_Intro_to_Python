# Define a function called sleep_in. It takes two parameters; The paramter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
#  sleep_in(False, False) → True sleep_in(True, False) → False sleep_in(False, True) → True

def sleep_in ():
    day = input("What day is it?: ")
    day.lower()
    week = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    vaca = input("Are you on vacation?: ")
    vaca.lower
    if (vaca == "yes"):
        return True
    else:
        for i in range (0, 6):
            if (day == week[i]):
                return False
            else:
                return True


print(sleep_in())