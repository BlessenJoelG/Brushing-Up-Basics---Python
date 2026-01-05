# in python a function is a block of code used to perform an action or task 
# a function can be defined by "def" keyword
def addTwo(x,y):
    add = x+y
    print(f"The addition of {x} and {y} is {add}")
x = int(input("Enter x value:\n"))
y = int(input("Enter y value:\n"))
addTwo(x,y)
addTwo(x=9,y=0.8)