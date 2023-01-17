# Find area of triangle with sidea 'a', 'b' and 'c'.
# Heron's Formula

a = float(input("Enter 'a' : "))
b = float(input("Enter 'b' : "))
c = float(input("Enter 'c' : "))

s = (a+b+c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print(f"The area of the triangle is : {area}")