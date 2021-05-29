# In this file you are to:
# Write a Program to check the greatest among 3 numbers.
# Write a Program to imitate a Traffic light. Think about the information you need to generate to
# make your program mimic the real world.

a=1
b=7
c=3

if (a>b):
    print("A is the greatest number")
elif(b>c):
    print("B is the greatest number")
else:
    print("C is the greatest number")


green = "green"
yellow = "yellow"
red = "red"

light = green

print(f"the light is {light} so you have to")
if(light == green):
    print("go")
elif(light == yellow):
    print("slow down")
else:
    print("stop")

