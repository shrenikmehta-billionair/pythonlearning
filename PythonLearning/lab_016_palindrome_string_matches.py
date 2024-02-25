def reverse_string(str):
    reverse_string = ""
    for i in str:
        reverse_string = i + reverse_string
    return  reverse_string
def palindrome_check(name_1,new_name):
    if name_1 == new_name:
        print(string_name, "The following string is a palindrome")
    else:
        print(string_name, "The following string is not a palindrome")


string_name = (input("Please enter the string name :"))
final_output = reverse_string(string_name) # calling reverse string function
palindrome_check(string_name,final_output) # calling palindrome function


"""if string_name == final_output:
    print(string_name, "The following string is a palindrome")
else:
    print(string_name, "The following string is not a palindrome")
"""