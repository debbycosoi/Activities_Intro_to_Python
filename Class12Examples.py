#Create a funtion calles sum. This function takes no parameters. Instead, ask the user for two numbers, addd those two numbers and return their sum

def sum():
    x = input("Tell me a number: ")
    y = input("Tell me another number: ")
    addition = int(x) + int(y)
    print(addition)
    return addition

sum()