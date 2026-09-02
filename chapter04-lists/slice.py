#when we use indexes, we get only one item at a time
#but with slices, we get multiple
#it has a starting and an ending point
#it STOPS before the ending point

spam = ['cat', 'bat', 'goat', 'bear']
print(spam[0:3]) #starts from 0 and stops before 3 so bear is not printed
print(spam[:2]) #no starting points means start from the beginning
print(spam[2:]) #no ending point means so go all the way to the end
print(spam[:]) #no starting and ending point just makes a copy of the list

#we make a copy of the list incase we don't want to change the original list
#so we make a copy and make chnages to it instead

newSpam = spam[:] #making a copy of the list and storing it
newSpam[0] = 'wolf' #making changes to the copied list instead of the original

print(spam)
print(newSpam) 
#guess the outputs