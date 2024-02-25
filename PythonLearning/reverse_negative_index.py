name = input("Enter the string")
reverse = ""
for i in range(len(name)-1, -1,-1):
    reverse = name[i] + reverse

print(reverse)

