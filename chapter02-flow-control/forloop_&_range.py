#unlike while loop which keeps running while a condition is true
#for loop goes through each item one by one

for fruit in ["apple", "mango", "banana"]: 
    print(fruit)

#fruit is a variable
#for loop goes through every item one by one as the loop goes on
#first the value of fruit is "apple" which gets printed, then in the second loop the value becomes "mango" and gets printed,
#and in the last loop the value of fruit becomes "banana" which gets printed. run to seee the output

for color in ["purple", "red", "blue"]:
    print(color) #guess the output

#with a string
for letter in "Python": #python goes through each letter one by one 
    print(letter) #and then print each letter one by one

word = "Python"

for letter in word:
    print("I found:", letter) #guess the output

#range is used to generate a sequence of numbers that a for loop can go through.
#range(stop) -> asuumes to start from 0 and stop before the number given
#range(start, stop) -> a number to start from and to stop before the given number
#range(start, stop, step) #step means to increase or decrease by the given number (like +2, -2)

for i in range(6): #when the start number is not given python assumes to start from 0, stop number is given so it will stop before the number 6
    print(i) #run to see the output

for number in range(10):
    print(number) #predict

for num in range(2, 8): #starts from 2 and ends "before" 8.
    print(num) 

for num1 in range(0, 11, 2): #the step tells the loop to change by how much. In this case in increases by 2 in each loop
    print(num1) #run to see the output
#prints "0" then increases by +2 so prints "2" in the second loop. and goes on like this and stops before 11

#for practice
#guess the outputs before running

for i in range(3, 8):
    print(i)

for i in range(2, 15, 3):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(5, 5): #a little tricky 
    print(i) 

#start at 5 and stop before 5. what will be the output?