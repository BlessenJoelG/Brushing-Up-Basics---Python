# # # break statement example:  the loop will terminate when it finds break statement
print("Break statement example\n")
i = 0
while(i < 12):
    if i == 9:
        break
    print("7*"+str(i),"=",7*i)
    i = i+1

# in korean or japanese i don't know but they treat 4 as unlucky number so they avoid using it in buildings and rooms etc.
print("\nContinue statement example\n")
i = 0
while(i<10):
    if(i == 4):
        continue
    print("it's",i,"floor")
    i = i+1
x =10
if(x is True):
    pass 
print("see nothing happened") # pass is used when you want to have empty block of code  
print("Actually their is a x with a value of 10")
