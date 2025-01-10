import art

print(art.logo)

def add(a,b):
    return a+b
def sub (a,b):
    return a-b 
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b


dict1={
    "+":add,
    "-":sub,
    "*": multiply,
    "/":divide
}

# operation=input("which operation do you want to do?")


# print(a)

next_number=True
first_num=int(input("What is Your first number? "))
while next_number:
    ops=print(
        "+\n",
        "-\n",
        "/\n",
        "*"
        )
    operation=input("Pick an operations: ")
    second_num=int(input("Enter Second number: "))
    a=dict1[operation](first_num,second_num)
    print(f"The answer is {a}")
    q=input(f"Type 'y' to continue calculating with {a} or type 'n' to start a new calculation: ")
    if q=='n':
        next_number=False
        print(f"The answer is {a}")
    else:
        first_num=a



