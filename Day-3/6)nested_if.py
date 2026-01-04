num = int(input("Enter a number:"))
if num > 0:
    print(f"The {num} is +ve")
    if num >0 and num <10:
        print(f"The {num} is between 0 & 10")
    elif num >10 and num<20:
        print(f"The {num} is between 10 & 20")
    else:
        print(f"The {num} is greater than 20")
else:
    print(f"The {num} is a -ve number")