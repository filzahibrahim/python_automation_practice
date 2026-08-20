message = "Outside"

def show():
    message = "Inside" #remember this? it is not reassigning a value to the message variable
    #but instead it is creating a different variable(local) 
    print(message)

show() #this prints "Inside"
print(message) #while this prints "Outside"

#so what should we do when we want to reassign a global variable inside a function
#we use the global statement

age = 18

def userAge():
    global age #this tells the python that I am referring to the global variable
    age = 21 #now we can reassign the value of the global variable
    print(age)

userAge() #so now when we call function, it prints the one from inside the function
#PLUS
print(age) #when we print the variable after the function ends, it still prints 21
#because even inside the function we were referring to the global one 

#another example 
score = 0

def addPoint():
    score = score + 1 #this will give an error bcz python thinks of it as different variable(local)
    #so it does not have a value yet
    print(score)

#addPoint() #will give an error
#but

def addPoint():
    global score
    score = score + 1 #this will work because now Python knows we are talking about the global variable
    #and reassigns it's value
    print(score)

addPoint() #increments by 1 everytime we call the function
addPoint()
addPoint()