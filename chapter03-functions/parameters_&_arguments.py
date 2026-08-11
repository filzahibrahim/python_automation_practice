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

introduce("Azusa", 20) #when calling the function. the argument should be in the same order as the parameter
#if you write 20 first. Python will think that "name" is an int and store 20 in it. and store "Azusa" inside the 
#parameter "age". This is why order matters.

#introduce("Azusa") 
#this will give an error because python expects the same number of arguments as parameters.
#when we call a function, we have to provide all the required information for its parameter.