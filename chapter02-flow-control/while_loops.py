#instead of printing everything one by one

print(1)
print(2)
print(3)
print(4)
print(5)

#we use while loops. For example:

count = 1

while count <= 5: #the loop continues as long as the condition is true
    print(count) #do this while the is true
    count = count + 1 #incrementing by 1 to move to the next number. (we can increment or decrement by any number)

#if we don't increment by 1, count will never increase remaining 1 forever which causes the condition
#to never become false causing an infinite loop which can crash a program.
# we need something that eventually make the condition of the loop false.
#when the condition becomes false we exit the loop and continue the program.

#we can also print it in descending order
count = 5
while count >= 1:
    print(count)
    count = count - 1

#this is out of the loop
print("Program end")
