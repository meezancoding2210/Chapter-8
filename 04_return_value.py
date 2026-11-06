# def greet(name, ending): #taking parameters
#     print("Have a good day,", name)
#     print(ending)

# a = greet("Meezan", "Thank you") #passing arguments. a has no return value
# print(a) #it would show None because there is no return value.

def greet(name, ending): #taking parameters
    print("Have a good day,", name)
    print(ending)
    return "Done" #It means the function would return the value to whichever variable wants it. In this case, it's a which needs a return value.

a = greet("Meezan", "Thank you") #passing arguments. a variale has a returned value from the function greet()
print(a) #it would show Done because it is returned

