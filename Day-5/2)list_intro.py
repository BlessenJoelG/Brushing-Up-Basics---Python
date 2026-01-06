# #in python list are the chaneable datatypes that is we can modify the existing list after its creation 
# #list is contained with elements seperated within "," and enclosed within [] square brackets
# friends = ["premik","blessen","joel","jaya"]
# print("friends","is a",type(friends))
# print("prem's friends are:",friends)
# print()

# #list index
# print("list index:\n")
# print("first friend of prem is:",friends[0])
# print("second friend of prem is:",friends[1])
# print("third friend of prem is:",friends[2])
# print("fourth friend of prem is:",friends[3])
# print()

# #negative indexing in list
# print("negative indexing in list:\n")
# print("last friend of prem is",friends[-1])
# print("second last friend of prem is",friends[-2])

# # checking items in list through membership operator
# find_friend = input("enter the friend you want to find: ")
# if find_friend in friends:
#     print(f"{find_friend} is one of prem's friend")
# else:
#     print(f"{find_friend} is not prem's friend")

# range of index in list
print("using range() in list")

coders = ["harry","Striver","vamsi bhavani","krushal","Abdhul bari"]
print("Top three favourite coders are:",coders[:3])
print("top 1 coder is:",coders[:1]) 
print("The last coder in the list is:",coders[-1:]) 
#  how to iterably add elements in a list

# using jump statement in list in indexing function which is optional
editors = ["nitishfx","telugutechicon","ahaaditya","sudhapusa"]
print(editors[:4:2])

print("list compreshension:\n")
# list comprehension is used to create a list through iterables like tuple,string,list etc
mates = ["Gopi","Guru","Bharath","Dhanush","Hrushi"]
mates_with_uo = [name for name in mates if "u" in name]
print("friends names with u in them:\n",mates_with_uo)

print("Square_numbers:\n")
odd_squares = [num*num for num in range(0,101) if num%2!=0]
eve_squares = [num*num for num in range(0,101) if num%2==0]
print("odd Squares of numbers from are",odd_squares)
print()
print("even Squares of numbers from are",eve_squares)
