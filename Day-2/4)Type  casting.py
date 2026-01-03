# Type casting is the process of converting one data type into an another data type of an existing ValueError
# their are two types of Type casting conversion they Are 
# 1)Emplicit Conversion: the programmer or user converts one data type to the other
# 2)Implicit Conversion: the interpreter automatically converts one data type to the other
# Example of Emplicit Conversion
a = "1"
b = "2"
print("Before Conversion",type(a),"+",type(b),"=",a+b)
print("After conversion",type(int(a)),"+",type(int(b)),"=",int(a)+int(b))

# Example of Implicit Conversion
x = 5.5
y = 6
print("the explicit conversion of ", type(x),"+",type(y),"=", x+y)