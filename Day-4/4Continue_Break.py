# # break statement example:  the loop will terminate when it finds break statement
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