# https://hangmanwordgame.com/?fca=1&success=0#/        --hangman game
# https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Step%205#R7VtdW6M4FP41ffZqfcpn62XrOOqszjrq6nq1TywpMALphrS28%2Bs3gYSPBBUtFLR7VXJIgJw35z0fSQfGUbg%2BwWDhXSAHBgN96KwHxpeBrmtDbUh%2FmGSTSiz7MBW42Hd4p1xw7f%2BCYiSXLn0HxqWOBKGA%2BIuycIaiCM5ISQYwRk%2FlbnMUlN%2B6AC5UBNczEKjSO98hXiod66Ncfgp91xNv1sT8QiA685nEHnDQU0FkHA%2BMI4wQSa%2FC9REMmPKEXu7ONnfB%2BaN98u1H%2FC%2F4a%2FrHzffb39OHfX3LkGwKGEbk3Y%2BGehTa4Ofq8ZKsVtduPNXWG%2FHoFQiWXF98rmQjFAgdqk%2FeRJh4yEURCI5z6RSjZeRA9pohbeV9zhFaUKFGhT8hIRu%2BOMCSICrySBjwuzXnxz82Rks8gy%2F0M%2FgyA9iF5IXJc1zZBAtrhWvvBKIQEryhHTAMAPFX5QUF%2BLp0s3657ukFV%2F8bUDYUKK5vJlc3Ch65tpnqnjyfwOsFSBTyRE24rNk5ighXu0anNnUDEMccqJhg9JgZBeudrfDhm0FZQUzg%2BkU1irs21zsnFIM3n3Lr1ITJeQXLNIfbK75yGaiK%2F1g28NLaftUG9K5soJqO9hoLrTMwfujfkHexml4g78dkeTY2rm7X2fR2qnq49snfbPiBxVv3hTtf1vzJSWMjGhGdbmEQa94X7%2BXDkpYYV6ntdnGvVPRwS5T50Evk08%2FOeDaLWzjPaiOJQNPv4qOktZJ9xvtteaiY8gmMIAYEsm9g8wORg0LG%2FAg7LLTDScsDkRuC6B8mjQ8Wm84c4NwPgiMUIJy81nAAHM9n2bDCHXs2hg%2FzHbpMTevaZwqqegbdOImfIzaFhwBEj7EQBtT4IWZXfpQh%2F9kCHKuMVoZCES1zl2hZvfCq29F0Y6ys1%2FTGdtPOuB5Nm0ZrNF3pfIyP4uXb9tb6TuA17N16YZWnJ%2FEjW%2F4eI%2BplDHFSkEkKNTCOuWtOafrzMbOcenbuR8f%2FM7PCuK8y82E3zGxZ9Ux3gjHYFLotWIf4%2BfdosgewhtK6Sp%2FYKC9o4y55Xyuwfu4D2sjudr44tVHTq3MrgrEVgjmLM%2FpPKB%2By3Gug2wGd1fSBkr7tsivhAtJAPe2fhOvGV9UveCh8WMav%2B4TWiF0Kuc0qYq8KucdtEbtufZS4qif2dVjTvnSzV%2FZ1qNjXFVwEbP0Lo0kS4GQp0pUohE0EWG0ZkxQkWXWDJDlxaa7YoOav9zBWlEenR8oaKldqIhRBqazDRSDw3Yg2Z1STFBVjypTlz0Aw4TdC33ESC62CpGy1baEylhjOVlGpIji9NYLbk%2FJwYwQnAoPXGa6zfcnKAoG9Hzi3V1ioAr5S02aXjkx8ZYFkz1EsavWBP08uIxYsLnCav%2FBK%2FUAp3QNMti%2Fc96b6LjtE87CmQ5TzxeawUqOO72jP%2FKEhZ82dO8QPU0ntiUMUSLzuEPVehfxGNzW6bUonWgnmHPW%2BAd0rnMVnF1j2FKx4Ypd8xjKqLJ2gJfOOaJ74zRU7%2FNjDkokulUzs7ksm6l7FyeTimEr%2BvD2%2B2i6aaEuL8o7CqGqvd6c7Cnqnhd23b%2Bg1xzKNF4bqbQuMZChb3tEzuk283%2BN%2BskY37sf8mO7HVOhwgpMkLBmb1BFtEDKiix7iRaI32RNlh29YkA%2F7WbuXy42jmgzanh9Ss6v9KzfKm5J21%2BmVoUZj%2B4eKXAUeDbtGRT2wvX%2BViHHfTEX1HHsHiilhou8Ok%2BfPeJcgueRV1NOsihrQmGzQq2Kqou%2B6UNVOmLRxTXffxO5iJTJq1nkD8whLHJHz5zzv%2F22VxmAYAofNKz9DQTzA8Gzk7Fx%2F8DKtEl5GBbllpy92gpdKblV4lbfZRcVm5qVbGj6LiSPE4JKOtxx8FuBkBrSqgLOrgLPeDBxt5n%2BDTfPc%2FM%2FExvF%2F#%7B%22pageId%22%3A%22t9u0Z-zH7QmrV4R77uba%22%7D
# -- flowchart 
# https://developers.google.com/edu/python/lists#for-and-in     --List docs
# https://developers.google.com/edu/python/lists#range          --List and Range()
# https://www.askpython.com/python/python-import-statement      --import

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
    
   