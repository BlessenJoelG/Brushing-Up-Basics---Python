print("Incrementing while loop\n")
i = 0
while(i < 5):
    print(i)
    i = i+1
print()
print("Decrementing while loop\n")
i = 5
while(i > 0):
    print(i)
    i = i-1
print()
# while with else statement
i = 0
while(i < 10):
    print(f"{i} is less than 10")
    i = i+1
else:
    print(f"{i} is greater than or equal to 10")
print()

print("enumalted do while loop\n")
i = 0
while(True):
    print(i)
    i = i+1
    if not(i <= 5):
        break