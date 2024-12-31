print("welcome to python pizza deliveries")
size=input("What Size of the pizza do you want ? S, M or L: ").upper()
pepperoni=input("Do you want to add pepperoni on your pizza Y or N? ").upper()
extracheese=input("Do you want extra cheese Y or N? ")
total = 0

if size=="S":
    total += 15
elif size == 'M':
    total += 20
else:
    total += 25


if pepperoni == 'Y' and size=='S':
    total+=2
else:
    total+=3
    
if extracheese=='Y':
    total+=1 

print(f"The total cost of your pizza is {total} ")
