#there are three boolean operators 
#and -> both conditions must be true
#or -> any one conditions can be true
#not -> inverts the value

age = 20
has_id = True

print(age >= 18 and has_id) #both conditions true so it evaluates to True

print(age >= 18 and not(has_id)) #one condition is false so it evaluates to False
#not inverted the value of has_id from True to False

print(age > 20 or has_id) #one condition is true so it evealutes to True
print(age >20 or not(has_id)) #OR is only false when both values are false

#practice
print(7 != 8 and 2 > 10) #guess the output f
print(5 > 3 and 10 == 10) #t
print(5 < 3 or 10 == 10) #t
print(not (5 > 3)) #f
print("cat" == "cat" and 20 >= 18) #t
print("dog" == "cat" or 100 < 50) #f
