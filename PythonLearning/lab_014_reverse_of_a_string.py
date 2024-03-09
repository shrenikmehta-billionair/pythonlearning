"""
name = "Shrenik"
name_1=len(name)
reversed_str = ""
for i  in name:
    reversed_str = i +reversed_str
print(reversed_str)
"""
name = "Shrenik"
name1 = len(name)
reversed_str = ""

for i in range(name1, -1, -1):
    reversed_str = name[i] + reversed_str

print(reversed_str)
