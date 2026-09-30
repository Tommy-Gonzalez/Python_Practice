#This program prompts the user to enter a series of numbers to be summed together
#Prompt the user to enter how many numbers to be entered
n = int(input("How many numbers would you like to sum: "))
list = []


#Using a for loop, constantly update the numbers within the list until we have n entries in the list
for i in range(0 , n):
    update = int(input("Enter a number in your list: "))
    list.append(update)

#Add together all elements within the list using the sum function
print(list)
sum_list = sum(list)
print(sum_list)