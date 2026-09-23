import numpy as np
#This program calculates coffee shop orders where the costs of coffee per pound are $10.50, with shipping being $0.86 per pound and a $1.50 fixed
#cost for overhead

coffee = 10.50 #per pound
order_ship_per_pound = 0.86 #Ship per pound
overhead = 1.50 #fixed cost for overhead


pounds = int(input("How much pounds of coffee would you like to buy? "))
shipping = pounds * order_ship_per_pound + overhead
total = (coffee * pounds + shipping)

print("Your total is $", total)