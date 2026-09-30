import numpy as np
import math

#This program is supposed to approximate the value of pi by summing the terms of the series: 
n = int(input("Enter the number of terms to sum the Gregory Leibniz series, the series used to approximate pi: "))


total = 0

for i in range(0,n):
    total += (-1)**n/(2*n+1)


result = 4 * total
print(result)


#Compare this number with the import math pi package and also the numpy package 