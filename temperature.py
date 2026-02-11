temp = float(input("Enter your temperature: "))
unit = input("Enter unit (C/F/K): ").upper()

if unit == 'C':
    fahrenheit = (temp * 9/5)+32
    kelvin = (temp + 273.15)
    print(f"{temp}°C = {fahrenheit:.2f}°F")
    print(f"{temp}°C = {kelvin}K")
elif unit == 'F':
    celsius =(temp-32)*5/9
    kelvin = ((temp - 32)*(5/9))+273.15
    print(f"{temp}°F = {celsius:.2f}°C")
    print(f"{temp}°F = {kelvin}K")
elif unit == 'K':
    celsius = (temp-273.15)
    fahrenheit = ((temp-273.15)*(9/5))+32
    print(f"{temp}K = {celsius:.2f}°C")
    print(f"{temp}K = {fahrenheit:.2f}°F")
else:
    print("Invalid")
