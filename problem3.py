import random
number = random.randint(1,10) 

while True :
    guess = int(input("please enter a number between 1 and 30"))
    if guess == number :
        print("your guess is correct! ")
        break
    elif guess<number :
        print("decrease your guess")
    else :
        print("increase your guess")
    
