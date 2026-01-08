def average(*nums):
    """this functions takes list of arguement and provides average of it"""
    sum = 0
    print(nums)
    for i in nums:
        sum = sum + i
    avg = sum/len(nums)  
    return avg
    # print(f"average is ",avg)
avgr = average(10,20,30,40,50)
print("average is:",avgr)
print("doc string of function average is:\n\n",average.__doc__,"\n")

# PEP-8 introduced for guidelines for python 
# zen of python is a python that can be run by "import this"
# that outputs:
'''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!''' 