import numpy as np
import matplotlib.pyplot as plt

#This program calculates the cost per square inch of a circular pizza, given it's diameter and price

diameter = int(input("Enter a diameter: "))
price = int(input("Enter a price: "))
radius = diameter / 2.0

Area = np.pi * radius ** 2
cost_per_square_inch = price / Area
print("The cost per square inch of a circular pizza is: $", cost_per_square_inch)