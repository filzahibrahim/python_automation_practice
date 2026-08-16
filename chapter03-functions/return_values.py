def add(a, b):
    print(a + b)

#add(2,3) #prints 5, right?
#the functions just takes the argument and prints it.
#but it doesnt give you the value, it just displays it which means we can not reuse it

result = add(2, 3)
print(result)  #returns None(means there is no value). the reason is that No value was stored
#inside result. 

#this is why we use "return" in functions when we want to reuse a value

def add(a, b):
    return (a + b)

answer = add(2, 7)
print(answer) #now it will print 9 because teh function gives you the value instead of just printing it!

#print() = just displays the value but you can't store or reuse it.
#return = gives you the value. Now you can do whatever you want with it!

#plus a function can only return once. 
#A functions STOPS after returning a value. so once you return a value, any code you write 
#after it doesn't matter! like:

def add(a, b):
    return a + b
    print("Done!") #wont run because it cones AFTER return

result = add(5, 3) #when i called the functions, ONLY the returned value matters.
print(result)

#BUT we can have multiple return statements IF ONLY ONE of them executes

def check_age(age):
    if age >= 18:
        return "Adult" 
    else: 
        return "Minor" 

#in this, only one return will execute this is why it works!!

#another example

def check_num(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
#only one value will return!
print(check_num(8))
print(check_num(-5)) 
print(check_num(0))