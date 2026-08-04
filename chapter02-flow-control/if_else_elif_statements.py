age = 20

if age >= 18: #python checks the condition if the user is older than 18 or not before executing the code
    print("You are an adult") #the space before print is indentation which shows that this line belongs to the if statement

age = 15

if age >= 18 : #colon is imp 
    print("You are an adult") #the condition is false so it skips this and ends up not printing 

print("Program Finished") #this is outside the indentation so python knows it doesn't belong to the if statement and is a standalone

if age >= 18:
    print("Adult")
else: #used as a other option when the first condition is false. 
    print("Minor")

temperature = 35

if temperature > 30: #do this IF true
    print("Its hot!!")
else: #or ELSE do this. skips ELSE when if is true
    print("Its cold")

age = 15

if age >= 18:
    print("Adult")
elif age >= 13: #lets you add another condition if the first condition is false
    print("Teenager")
else: 
    print("Minor")

score = 75

if score >= 90: #checks -> false -> moves on
    print("A")
elif score >= 80: #checks -> false -> moves on
    print("B")
elif score >= 70: #checks -> true -> executes
    print("C")
elif score >= 60: #skips
    print("D")
else: #skips
    print("F")

score = 85
age = 20

#we can also said muiltple condition using "and" and "or"
#for example
if score > 80 or score > 90: #if any one of these conditon is true it will print great work
    print("Great Work")

if age > 18 and score > 80: #with "and" both conditions has to be true for it to run
    print("You will get a job!") 