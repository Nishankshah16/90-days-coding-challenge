import Hangmanart as Hangmanart
import random

print(Hangmanart.title)

lives=6
assigned_word= random.choice(Hangmanart.word).lower()

placeholder=""
for position in range(0,len(assigned_word)):
    placeholder+="_"
print(placeholder)

correct_letters=[]
game_over=False

while not game_over:
    guess= input("Guess the letter : " ).lower()[0]
    display=""
    for letter in assigned_word:
        if letter == guess:
            display +=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"

    print(display)
    print(Hangmanart.HANGMANPICS[lives])

    if "_" not in display:
        game_over=True
        print("you win")
    elif guess not in assigned_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You lose")
    
   