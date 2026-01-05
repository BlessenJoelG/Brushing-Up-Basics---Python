x = int(input("Enter your age:\n"))
match x:
    case x if x>0 and x<=18:
        print("You are an teenager.")
    case x if x>18 and x<=30:
        print("You are a adult")
    case x if x>30 and x<65:
        print("you are a uncle")
    case x:
        print("You are a grandpa")
    