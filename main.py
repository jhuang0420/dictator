# This python file takes your name and age as input and tells you whether you're
# young or old according to a very precise mathematical formula contrived by Harvard graduates.

name = input("Please enter a name: ")
while True:
    try:
        age = int(input("Please enter the age in years: "))
        if (age < 0): raise Exception("Sorry, no numbers below zero")
        elif (age <= 20): print(name + " is young.")
        else: print(name + " is old.")
        break
    except:
        print("Please enter a valid age") 
