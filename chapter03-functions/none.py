#None is a data type that has no value
#None is not the same as zero, false or "" (an empty string). Just no value or the value is absent

#It is its own data type = NoneType
x = None
print(type(x))

#Python always return something. But when it doesnt have anything to return, it shows None
#it also shows none when you return with nothing after it

def check_age(age):
    return 
print(check_age(18))

#None is also used as a default parameter

def greet(name = None):
    if name is None:
        return f"Hello! stranger"
    else:
        return f"Hello, {name}"

print(greet("Azusa"))
print(greet())