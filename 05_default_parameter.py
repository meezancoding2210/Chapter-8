def greet(name, ending="Thank you"): #Here, we have taken `thank you` as a default parameter. It means if there's no argument for `ending`, then `thank you` would be printed by default. 
    print(f"good day, {name}")
    print(ending)

greet("Meezan", "Thank you") #Both arguments are given. 
greet("Zeyan") #Only one argument. 