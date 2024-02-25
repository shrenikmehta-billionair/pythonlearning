def reverse_string(str):
    reverse_string = ""
    for i in str:
        reverse_string = i + reverse_string
    return  reverse_string

string_name = "shrenik"
final_output = reverse_string(string_name)
print(final_output)