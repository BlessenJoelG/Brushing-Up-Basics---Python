# in string datatype their are many operators which help us to maipulate strings which are immutable hence they return and modified 
#  string than modifying original string
"""some of the operators are as follows
 1)concatenation(+)
 2)repetition(*)
 3)slicing([start:end:step])
 4)membership(in , not in)
 5)escape sequence(\)
 # 6)raw string(r'')
 7)string methods(lower(),upper(),title(),capitalize(),find(),replace(),split(),join(),strip() etc)
 8)formatted string(f'')"""
a = "Blessen"
b = "Joel"
print(f"Concatenation of {a} and {b} is : {a+"\t"+b}")
print("Repetition of a:",a*3)
print("ssen"not in a)
#string methods 
x= "Premik is only Premik and a 10 on 10"
y= "Premik"
print("uppercase of x is:",x.upper())
print("lowercase of x is:",x.lower())
print("starts with 'pre'",x.startswith("pre"))
print("ends with 'mik'",x.endswith("mik"))
print("number of ocuurences of 'premik'",x.count('Premik'))
print("splitting method in string:",x.split(" "))
print("replacing premik with joel:",x.replace("Premik","joel"))
print("finding method in string:",x.find("Prem"))
print("isalpha method in string:",y.isalpha())
y = "Premik73"
print("isalphanum method in string:",y.isalnum())
x= "premik is only premik and a 10 on 10"
print("capitalize method in string:",x.capitalize())
print("title method in string:",x.title())
print("strip method in string:",x.strip("premik is"))
#these are the basic initially tend to be learnt and known method to 
#a beginner in python read and practice again and again to remember