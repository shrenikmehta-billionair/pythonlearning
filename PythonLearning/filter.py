numbers = [1,2,3,4,5]

"""even_numbers = list(filter(lambda x:x%2 ==0,numbers))
print(even_numbers)
"""
def even(num):
    return num % 2 == 0


even_number = filter(even,numbers)
print(list(even_number))



