# https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D             
# -- flowchart
# https://ascii.co.uk/art       -- ASCII Art


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