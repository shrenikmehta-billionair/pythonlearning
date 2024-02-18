"""
number = int(input("Enter the number"))
num1 = 0
num2 = 1
num3 = 0
i = 1
print(num1)
print(num2)
for i in range(number):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3)
    i = i + 1
"""


### part 2

a, b= 0, 1
while a <10:
    print(a, end=" | ")
    a, b = b, a+b





