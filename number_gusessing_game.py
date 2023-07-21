import random
Cnumber=random.randrange(1,101) # computer number logic
userInput=int(input("Enter your Number:----"))
if userInput>Cnumber:
    print("Computer Number",Cnumber)
    print('Your guess number is too high')
elif Cnumber>userInput:
    print("Computer Number",Cnumber)
    print("Your guess is too low")

else:
    print("Computer Number",Cnumber)
    print("Your guess number is equal")    
    

