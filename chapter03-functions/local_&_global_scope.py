#scope is about where a variable was created and where can it be accessed from
#now there are two types of scope
#Local Scope: a variable that is created inside a function. It can only be accessed when the function
#is running and can only be accessed by the function. When the function ends so does the local variable

def greet():
    message = "Heyyyy" #a local variable created inside the function
    print(message)

greet() #the function will run and the message will be accessed 
#but
#print(message) #this will cause an error because that variable does not exist out here

#Global Scope: they are created outside of the function and they can be accessed inside the function
#as well BUT they can not be changed inside the function without a special permission

name = "Azusa" #global variable

def greet():
    print(f"Hello {name}") #can access the global variable!

greet()

message = "outside" #global variable

def show():
    message = "inside" #local variable #this is not changing the global variable but instead
    #making a different variable that is local, totally different from global
    print(message)
#any variable inside function is a local variable unless you tell Python otherwise

show() #prints "inside" bcz it is calling the function.
#after the function ends, that message = "inside" also ended
#so when i ask to print message again
print(message) #this time it prints "outside" because only one "message" variable exists outside
#the function