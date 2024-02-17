import math
radius = float(input("enter the radius:"))
print(math.pi)
area = math.pi*pow(radius,2)
area_rounded = round(area,2) # 2 means upto 2 digit are decimal are rounded
print("Area of circle = ", area_rounded)

