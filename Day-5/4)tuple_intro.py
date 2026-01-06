#tuple is a datatype in python in wich it is immutable that means the elements or values in the tuple cannot be changed 
# tuple is enclosed within paranthesis and elements are seperated by ','
tup = ("Blessen Joel",73,"B.tech","Ai")
# print("tuple:",tup)
# print(tup[0],"is the name of the student")
# print(tup[1],"is the students roll no")
# print("The student is pursuing his",tup[2],"in",tup[3])
# #slicing in tuple
# tupler = (9,8,4,8,1,2,7,6,5,3,4,8)
# print(tupler[:5])
# print(tupler[3:])
# print(tupler[0:12:2])
# tup = ("Blessen Joel",73,"B.tech","Ai")
# print(tup[0:2])
# print(tup[-2])

#finding an element in tuple 
if "Blessen Joel" in tup:
    print("A student of 'Ai' is present")
else:
    print("A student of 'Ai' is not present")
