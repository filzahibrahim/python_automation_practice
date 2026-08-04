count = 1

while count <= 10: # the loop works normally when the break condition is false
    print(count)

    if count == 5:
        break  #it means to STOP the loop immediately when the if condition becomes true
    #break ends the loop and exits it when the condition becomes true. 

    count = count + 1

count = 0
while count < 5:
    count = count + 1 

    if count == 3:
        continue #it means to skip THIS iteration and go back to the top of the loop
    #it basically means to skip wtvr comes after it and then continue the loop 

    print(count)  #so due to continue, this part is skipped and 3 doesnt get printed and we continue the loop
    #run this progranm to understand it better

# practice - guess the output
count = 11
while count > 1:
    count = count - 1
    #can also be written as
    #count -= 1

    if count < 8:
        break

    print(count)

#we can use 
#while True
#it will run keep repeating 
#but we can use break in it so it eventually stops
#we use while True when we want something to keep repeating until we ask it to stop(break)