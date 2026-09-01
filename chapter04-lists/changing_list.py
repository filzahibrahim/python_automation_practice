#we can also change items from a list

fruits = ["banana", "mango", "apple"]

#if we want to replace "mango" with "orange"
#we can just

fruits[1] = "orange" #this means to just change whatever is at index 1 to "orange"

#list are mutable, which means they can be changed
#so we can change any item 

numbers = [20, 40, 60 , 80]
print(numbers)
numbers[1] = 400
numbers[3] = 800
print(numbers)

#changing the items in a list doesn't create a new list. 
#the list stays the same and only the items are changed