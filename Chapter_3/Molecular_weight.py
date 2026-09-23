import numpy as np
import matplotlib.pyplot as plt

#This program determines the molecular weight of a hydrocarbon based on the number of hydrogen, carbon, and oxygen atoms


#Atom             #grams/mole
Hydrogen_weight = 1.0079
Carbon_weight = 12.011
Oxygen_weight = 15.9994

num_H = int(input("Enter the number of Hydrogen atoms: "))
num_C = int(input("Enter the number of Carbon atoms: "))
num_O = int(input("Enter the number of Oxygen atoms: "))

total_weight = (Hydrogen_weight * num_H) + (Carbon_weight * num_C) + (Oxygen_weight * num_O)

print("The total molecular weight of the hydrocarbon atoms are: ", total_weight, "grams/mole.")