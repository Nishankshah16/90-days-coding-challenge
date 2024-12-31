import random 
rock='''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ 
'''
       

paper='''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_| 
'''

scissors='''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \\
|___/\___|_|___/___/\___/|_|  |___/
'''

list1 = [rock, paper, scissors]
b = True
while(b):

    user = int(input("What do you choose? 0 for rock, 1 for paper and 2 for scissors. "))
    print(list1[user])
    computer = random.randint(0,2)
    print("Computer chose:", list1[computer])

    if user <0 or user >2:
        print("Invalid number! you Lose")
    elif user == 0 and computer == 2:
        print("You win!!")
    elif computer == 0 and user == 2:
        print("Computer wins!!")
    elif user == computer:
        print("Match Draw")
    elif computer > user:
        print("Computer wins!!")
    elif user > computer:
        print("You win!!")
    
    a = input("Do you want to play again?Y or N ").lower()
    if(a == 'y'):
        b = True
    else:
        b = False
0