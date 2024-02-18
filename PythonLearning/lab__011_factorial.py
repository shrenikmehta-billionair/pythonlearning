factorial_n = int(input("Enter a number"))
factorial_n1 =1

'''for i in range (factorial_n):
    factorial_n1 = factorial_n * factorial_n1
    factorial_n = factorial_n - 1
print(factorial_n1)
'''

# Part - 2
if factorial_n < 0:
    print("fact")
elif factorial_n==0:
    print("fact = ", 1 )
else:
    fact = 1
    for i in range(1,factorial_n+1):
        fact = fact * i
    print("fact is ", fact)
