import numpy as np
import matplotlib.pyplot as plt

#This program calculates the slope of a line that passes through two points
#Then calculates the distance between them

x1 = int(input("Enter your first x coordinate: "))
y1 = int(input("Enter your first y coordinate: "))

x2 = int(input("Enter your second x coordinate: "))
y2 = int(input("Enter your second y coordinate: "))

slope = (y2 - y1)/(x2-x1)

print("First coordinate points: ", x1, y1)
print("Second coordinate points: ", x2, y2)

print("The slope of the line between your two points is: ", slope)



distance = np.sqrt( ( x2 - x1 )**2 - ( y2 - y1 )**2 )
print("The distance of the entered coordinates is: ", distance)