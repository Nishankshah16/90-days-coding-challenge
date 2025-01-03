import Hangmanart as Hangmanart
import hangman_words as Hangmanword
import random

print(Hangmanart.title)

lives=6
assigned_word= random.choice(Hangmanword.word).lower()

placeholder=""
for position in range(0,len(assigned_word)):
    placeholder+="_"
print("Word to guess: ", placeholder)

correct_letters=[]
game_over=False

while not game_over:
    print(f"******************************{lives}/6 LIVES LEFT ******************************")
    guess= input("Guess the letter : " ).lower()

    if guess in correct_letters:
        print(f"You have already guessed {guess}")

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
        print("***************You win****************")
    elif guess not in assigned_word:
        lives-=1
        print(f"You guesses {guess}, thats not in the word. You lose a life.")
        if lives==0:
            game_over=True
            print("You lose")
    
   