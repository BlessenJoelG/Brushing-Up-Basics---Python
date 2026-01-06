# main and need to be known methods of list are 
# 1.append
# 2.sort()
# 3.count()
# 4.index()
# 5.insert()
# 6.extend()
# 7.copy()
# concatenate is an operation of list
nums_list = [73,858,3,74,21,12,18,99,69]
# copy() function creates duplicate copy of the existing list
nums_copy = nums_list.copy() #this will create a copy of nums_list
nums_copy.append(143)
print("this is the list of nums_copy appended with'143':\n",nums_copy)
print("this is the list of nums_list didn't got any change:\n",nums_list)
print(nums_list)
#append()function
nums_list.append(93)
nums_list.append(93)
nums_list.append(93)
print("Appending the list with '93':\n",nums_list)
# sort()function
nums_list.sort()
print("The sorted order of list is:\n",nums_list)
# reverse parameter in sort() functiom
nums_list.sort(reverse=True)
print("the reverse order of the list using sort() function is:\n",nums_list)
nums_list.sort()
print("sorted again for checking reverse function:\n",nums_list)
# using reverse() function
nums_list.reverse()
print("reversing the list using reverse() function:\n",nums_list)
nums_list.insert(4,"Ma")
print('After inserting a string named "Ma" in the 4 index of list:\n',nums_list)
print('number of times "93" occured in the list is :',nums_list.count(93))

# new list creation
strings_list = ["raghu","ravi","hari","bhaskhar","kiran"]
nums_list.extend(strings_list)
print("extending nums_list with strings_list:,i.e,\n",nums_list)

list1 = ["ravi",143]
list2= ["hari",145]
print("print concatenation of list1 + list2",(list1+list2))
print("repetition of list1 for 3 times is:",list1*3)