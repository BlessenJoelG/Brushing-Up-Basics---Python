#printing sequence of characters in a string through for loop
name = input("Enter your nickname:\n")
print(f"Your name is {name}")
for char in name:
    print(char)
# accessing element in a list
heroes = ["iron man", "black widow", "captain marvel", "thor", "dr-doom"]
for hero in heroes:
    print(hero)
    for char in hero:
        print(char)
    print()
#accessing elemts in tuple()
friends = ("premik","joel","blessen","prem") 
for drohi in friends:
    print(drohi)  
print()
#rangefunction()
# syntax: range(inclusve,exclusive,step)
# iterating through a range of numbers
print("The even numbers will be:")
for i in range(0,10,2):
    print(i)
print()
print("The odd numbers will be:")
for i in range(1,10,2):
    print(i)

# print over 20000numbers
for i in range(0,20001,1):
    print(i)