unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = (9 * temp) / 5 + 32
    print(f"Temperature in Fahrenheit is: {temp} F")
elif unit == "F":
    temp = (temp - 32) * 5 / 9
    print(f"Temperature in Celsius is: {temp} C")
else:
    print(f"{unit} is an invalid unit of measurement.")