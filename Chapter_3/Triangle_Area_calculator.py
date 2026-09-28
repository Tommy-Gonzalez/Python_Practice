import numpy as np
import matplotlib.pyplot as plt

#This program calculates the area of the triangle with the three sides given as input

a = int(input("Enter side a of the triangle: "))
b = int(input("Enter side b of the triangle: "))
c = int(input("Enter side c of the triangle: "))

#s is the semi parameter of the triangle, which is half of the total parameter
s = (a + b + c)/2

area = np.sqrt( s * ((s-a) * (s-b) * (s-c)) )

print("The area of your triangle is: ", area)