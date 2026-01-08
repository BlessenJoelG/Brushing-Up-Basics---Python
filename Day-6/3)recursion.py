# recursion is basically a function calling itself
def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*facto(n-1)
print("factorial of 5 is",facto(5))

# similarly for fibbinoci series

def fibbinoc(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibbinoc(n-1)+fibbinoc(n-2)
i = int(input("enter number:\t"))
print(f"fibbinocial no of {i} is",fibbinoc(i))
