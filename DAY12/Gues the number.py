# https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20         --ASCII text
# https://pythontutor.com/visualize.html#mode=edit                                      -- Tutor (debug)

import random

print("Welcome to the number guessing game ")

print("I am thinking of a number bewtween 1 to 100")

difficulty=input("Choose the difficulty type 'easy' or 'hard'? ").lower()

correct_number= random.randint(1,100)

chances=0

def guess(chances, correct_number):
    
    flag =False
    while(chances >= 1):
        print(f"You have {chances} attemptes remaing to guess the number ")
        guess=int(input("Make a guess: "))

        if guess==correct_number:
            flag =True
            break
        elif guess> correct_number:
            print("To high\n Guess Again")
            chances-=1
        elif guess<correct_number:
            print("To low\n Guess Again")
            chances-=1

    if flag == True:
        print("You win")
    else:
        print("You lose")
        print(f"The number was {correct_number}") 
    
        

if difficulty == 'easy':
    chances=10
    guess(chances,correct_number)
else:
    chances=5
    guess(chances,correct_number)

