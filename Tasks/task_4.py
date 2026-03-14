# to calculate the area of the circle

import math

radius = float(input("Enter the radius of the circle (in cms): "))

area = math.pi * radius**2

print(f"The area of the circle is {round(area, 2)} cm^2.")