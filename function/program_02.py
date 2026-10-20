# Function Program 2

import math
def rectangle(width, length):
    return width * length
def triangle(height, base):
    return 0.5 * height * base
def circle(r):
    return math.pi * r * r
w = float(input("Enter width: "))
l = float(input("Enter length: "))
print("Area of rectangle:", rectangle(w, l))
h = float(input("Enter height: "))
b = float(input("Enter base: "))
print("Area of triangle:", triangle(h, b))
r = float(input("Enter radius: "))
print("Area of circle:", circle(r))
