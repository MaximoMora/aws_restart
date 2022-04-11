print("welcome to my game")
print("THe rules are simple,  if you guess the number you win")

import random

random_number = random.randint(0,10)
iqual = False


while iqual != True:
    user_number = int(input("number: "))
    if user_number == random_number:
        print("you guess")
        break 
    elif user_number > random_number:
        print("number is lower")
    elif user_number < random_number:
        print("number is greted")
    
    
    
for x in 