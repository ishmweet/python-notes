# to calculate the hypotenuse of a right angled triangle

import math

a = float(input("Enter side A (in cms): "))
b = float(input("Enter side B (in cms): "))

c = math.sqrt(a**2 + b**2)

print(f"C = {round(c, 2)} cm.")