#This program prompts the user to enter a set of natural numbers. If the numbers are not natural, the program will prompt the user
#to reattempt entering a natural number
12
n = int(input("Enter a natural number: "))
j = int(input("Enter another natural number: "))

if n < 0:
    print("Error. You have entered a number less than zero, invalidating the prompt for the request of the first natural number.")
    n = int(input(print("Enter the first natural number again: ")))
if j < 0:
    print("Error. Your second number less than zero, invalidating the prompt for the request of the second natural number.")
    j = int(input(print("Enter the second correct natural number: ")))

The_sum = n + j

print("The sum of your two natural numbers is: ", The_sum)