#This program is  supposed to find the sum of the cubes of the first n natural numbers, where the value of n is provided by the user

n = int(input("Enter a natural number: "))

while n < 1:
    print("Error: a natural number must be 1 or greater")
    n = int(input("Enter a natural number again: "))

total = 0
for i in range(1, n+1):
    total += i ** 3


print("As the summation begins cubing our input from 0 to ", n, " the total is: ", total)