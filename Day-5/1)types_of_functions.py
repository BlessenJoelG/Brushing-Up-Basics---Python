print("Required arguement functions:")
def avg(a,b):
    avg = (a+b)/2
    print(f"average of {a} and {b} is {avg}\n")
avg(5,6) #required arguement

print("default arguement functions:")
def avg1(a=5,b=5):
    avg = (a+b)/2
    print(f"average of {a} and {b} is {avg}\n")
avg1() #default arguement
avg1(10,) # checking with single arguement and a default arguement

print("Arbitary arguement functions i.e tuple:")
def avg2(*nums):#creates a tuple by "*nums"
    sum = 0
    for i in nums:
        sum = sum + i
    avg2 = sum/len(nums)
    return avg2
avg = avg2(5,6,7,8,9) # arbitary arguement
print(f"average of 5,6,7,8,9 is {avg}\n")
 # arbitary arguement with key value pairs

print("Arbiatary arguement functions i.e dictionary:")
def avg3(**name):
    print("hello!!",name["fname"],name["mname"],name["lname"])
    print("how is everything going on")
avg3(fname=input("enter your first name:\n"),mname=input("enter your middle name:\n"),lname=input("enter your middle name:\n"))
    