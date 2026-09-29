#This program prompts the user to enter a set of natural numbers. If the numbers are not natural, the program will prompt the user
#to reattempt entering a natural number

n = int(input("Enter a natural number: "))

while n < 1:
    print("Error: a natural number must be 1 or greater")
    n = int(input("Enter a natural number again: "))

total = 0
for i in range(1, n+1):
    total += i

print("As the summation begins from 0 to n, the total is: ", total)