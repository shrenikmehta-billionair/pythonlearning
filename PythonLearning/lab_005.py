"""
1) Explain the difference between the = operator and the == operator in Python.
2) What does the ** operator do in Python, and how is it used?
3) What does the ^ operator do in Python, and in what context is it commonly used?
"""
"""
ANS 1 The = operator is for assigning value to the given variable and == operator is for comparing two values of the variable
ANS 2 ** is kind of raise to operator i.e. 3**2 means 3*3 = 9

"""
# Generating area for a circle with radius as a input from user
import math
pie_value = 3.14
radius = float(input("Enter the radius for a circle : "))

Area_of_a_circle = (pie_value * radius * radius)
#area = 3.14 * pow(radius,2)
print("The area of circle is ", Area_of_a_circle)

# area = 3.14*pow(radius,2)
