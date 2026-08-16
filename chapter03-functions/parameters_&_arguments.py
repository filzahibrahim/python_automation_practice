#we give our function a variable that can recieve information
def greet(name): #name is a variable inside function waiting to receice a value. Also called "parameter"
    print(f"Hello! {name}") 

greet("Azusa") #Here Azusa is an "argument". This is the value of the variable/parameter 
#we write the value(argument) of the variable(parameter) when calling the function

#parameter - argument lets us have diff value using the same function multiple times

greet("Emma")
greet("Sarah") #same function, diff values

#we can also have multiple parameters

def introduce(name, age): #we can ask for more than one value
    print(f"My name is {name} and I am {age} years old")

#python doesnt know that name should be a string and age should be an int. It just matches the order of the parameters
introduce("Azusa", 20) #when calling the function. the argument should be in the same order as the parameter
#if you write 20 first. Python will think that "name" is an int and store 20 in it. and store "Azusa" inside the 
#parameter "age". This is why order matters.

#introduce("Azusa") 
#this will give an error because python expects the same number of arguments as parameters.
#when we call a function, we have to provide all the required information for its parameter.

#we can have also have parameters with an default value

def introduce(name, age = 18): #if we dont give age a value python will just print 18 instead
    print(f"My name is {name} and I am {age} years old")

#so now this won't give an error
introduce("Azusa") #we didnt give a value for age when calling the function
#but there is alr a default value for age so it won't throw an error

#we can also give age a value even if there is alr a default value
introduce("Azusa", 20) #python just assigns age the new value we gave in our argument

#default value works as a backup. if we dont give a value in our argument. Python uses the default value but if
#we do give a value in our argument. Python assigns that value to the parameter age and prints it.

#another example

def greet(name, message = "Hello!"): #the default parameter always come at the end
    print(f"{message}, {name}")

greet("Azusa")
greet("Sarah", "Hiiii!")
greet("Emma", "Morning!")

#Now "Keyword Argument"
#remember how i had to match the order of the argument with the parameter
#instead of worrying about the order we can just use the keyword in the argument. like:

greet(message="You are a X-women!", name="Frost") #see the order is different from the parameter
#but because we used the keyword, Python knows which argument belongs to which parameter!
#we can also have a mix of keyword and positional argument

greet("Frost", message="You are so cool!") #Frost goes into name due to positional argument then the message 
#one is direct with a keyword
#BUT

#greet(message="You are so cool!", "Frost") 
#This is not allowed. A positional argument can not come after a keyword argument
#this is the rule of order!