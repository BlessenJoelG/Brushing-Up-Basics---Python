# Type casting in pyhton is basically changing the datatype of a variable to the other one 
# their are 2 types of type casting in python they are
"""1)Explicit conversion : programmer or user initiates to convert the datatype of the variable
2)Implicit conversion : according to the higher and lower order of python conversion are made 
through python from lower to higher levels of datatype"""
a = "1"
b = "2"
print(int(a) + int(b))
print(float(a) + float(b))
print(bool(a) + bool(b))

c = 5.5
d = 1
print(type(c),"+",type(d),"=",type(c+d))
e = "hello"
f = [1,"a",0.5]