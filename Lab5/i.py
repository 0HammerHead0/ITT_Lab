import copy
a=[1,2,3,4,5,4,3,2,1]
b = copy.copy(a)
# rev_a = a[::-1]
b.reverse()
if(a==b):
    print ("Palindrome")
else:
    print("Not Palindrome")