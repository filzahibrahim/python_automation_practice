#you know when you write an integer when the program expects a string?
#you get an error because the program crashes
#that is when we use exception handling, to prevent those programs from crashing due to an error
 
try:
    result = 10 / 0 #in try we put the code that might cause an error
except ZeroDivisionError:
    print("You can not divide by 0") #and if that error does happen, this will run instead of the program crashing

#we can also handle multiple error
def divide20(number):
    try:
        return 20 / number
    except TypeError:
        print("Write a number")
    except ZeroDivisionError:
        print("Can't divide by zero")

print(divide20(5))
print(divide20(0)) #the function will run and except block will end with it
print(divide20("hello"))
print(divide20(0)) #will give back none because we did not return anything in the except block

def divide20(number):
    try:
        return 20 / number
    except TypeError:
        return "Write a number"
    except ZeroDivisionError:
        return "Can't divide by zero" #now we used return so we can call this multiplt times and will not return "None"

#practice ques

def collactz(number):
    if number % 2 == 0: #check even or not
        result = number // 2 #divides it
        return result #returns the value
    else: #else it's odd
        result = 3 * number + 1  #multiple the num by 3 and adds 1
        return result #returns it

num = None #giving it no value

while True: #keeps running
    if num is None: #checks the condition #if the num is not None, this block is skipped
        try: #exception handling 
           num = int(input("Write a number:")) #checks the input of this code
        except ValueError: #the exception
           print("Please write a number") #orints this when the user writes anything other than an integer
           continue #this goes back to try and ask the user again for input
    if num == 1: #condition #if the number is not 1, it skips this block
        print("Done") #prints this when num becomes one
        break #breaks out of the loop
    print(num) #prints whatever the number is 
    num = collactz(num) #whatever the number is becomes and argumnet and calls the function. 
    #the returned value is stored and becomes the new value of num that goes back up 
    #the loop keeps on running until we get 1 and breaks out of it