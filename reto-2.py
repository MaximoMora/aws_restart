
import random

number_random = random.randint(0,10)

number = 0
    
while number != number_random:
    number = int(input("number: "))
    if number == number_random:
        print(f"adivinaste el numero {number}")
    
    elif number > number_random:
        print("el numero es mas pequeño")
        continue
        
    else:
        print("el numero es mas grande")
        continue
    