print("Welcome to Treasure Island\nYour mission is to find the treasure.")

a=input("Do you want to go left or right? ").lower()

if a == 'left':
    print("You have come to lake. There is an island in the middle of the lake")
    b=input("Type wait to wait for boat. Type 'Swim' to swim across").lower()
    if b == 'wait':
        print("You have come to island un harmed. There is a house with three doors")
        c= input("One red , one yellow, one blue. Which color do you choose? ").lower()
        if c == 'yellow':
            print("You win")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")