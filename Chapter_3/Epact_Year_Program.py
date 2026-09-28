import numpy as np
import matplotlib.pyplot as plt

#The Gregorian epact is the number of days between January 1st and the previous new moon. The value is used to figure out
#the date of Easter. It is calculated by integer arithmetic.


year = int(input("Enter a 4 digit year: "))
C = year//100

epact = ( 8 + ( C // 4 ) - C + (( 8 * C + 13 ) // 25 ) + 11 * ( year % 19 )) % 30
print("The value of your epact is: ", epact)