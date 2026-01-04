""""in python range and indexing works like [inclusive:exclusive] 
 where exclusive returns one less than the value placed
negative slicing works from the end of the string where -1 
 is the last character of the string"""

x = "Premik learns Python again from scratch"
print(x[0:])
print(x[0:7])
print(x[14:20],"is created by guido van rossum")
print(x[14:20],"is loved by",x[0:7])

print("length function in python:\n uses 'len()' & returns a number")
y = "Blessen"
print("length of",y,"is",len(y))
print("length of",x,"is",len(x))
""""negative slicing works different it uses len of the string -the value placed"""
z = "Sanjana"
print("negative slicing of z[1:-3]:",z[1:-3])
print("negative slicing of z[-3:-2]:",z[-3:-2])
print("negative slicing of z[-1]:",z[:-1])
print(y[1:-1])
print(z[-1:])