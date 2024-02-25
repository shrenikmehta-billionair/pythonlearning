"""
name = "Shrenik"
name_1=len(name)
reversed_str = ""
for i  in name:
    reversed_str = i +reversed_str
print(reversed_str)
"""
name = "Shrenik"
reversed_str = ""

for i in range(1, 0, 1):
    reversed_str += name[i]

print(reversed_str)
