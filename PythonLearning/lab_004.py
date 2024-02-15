import sys
var_input_shrenik = 1
# unorderd list with duplicate items
my_list =[1,2,3,4,5,4]
print(my_list)
# unorderd list with no duplicate items
my_set ={1,2,3,4,5,4}
print(my_set)

age =65
number_teen = 0b1010 # binary number
c =  0o130 # oct number
d = 0x12c # hexadecimal number



a=5
b=5
print (a is b) #  Identity Operator in Python is a special comparison operator used to check if two variables reference the same object in memory. They are different from the equality operators that compare values. In Python, there are two identity operators: is and is not .
print(id(a))
print(id(b))
print(sys.getsizeof(5))

"""list = [1,2,3]
list1 = [1,2,3]
print(id(list))
print(id(list1))

print (list is list1) # list are not stored at the same object in the memory so is operator gives result as false
"""



