randumbs = (9,8,4,8,3,2,7,6,8,3)
print(randumbs,"is a",type(randumbs))
tup_modify = list(randumbs)
print(tup_modify,"is a conversion of",type(randumbs),"to",type(list))
tup_modify.pop()
tup_modify.append(99)
tup_modify.insert(2,"Sanjana")
randumbs = tuple(tup_modify)
print("the modified tuple through list is:",randumbs)

#methods of tuple
#count()
#index()
# operations are concatenate()

randumbs = (9,8,4,8,3,2,7,6,8,3)
i = int(input("Enter the num u want to check:\n"))
print(f"The number {i} has occured {randumbs.count(i)} times in this tuple")
#count() function returns the first occurence index number of the given element
print(f"index of 8 in the list is {randumbs.index(8)}")