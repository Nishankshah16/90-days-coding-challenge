import art 
import gamedata
import random 


def choice():
    return random.choice(gamedata.data)



# def print_choice(a):
#     print(f"{a['name']}, a {a['description']}, from {a['country']}")

def format_data(account):
    account_name= account['name']
    account_descr=account['description']
    account_country=account['country']
    return f"{account_name}, a {account_descr} from {account_country}" 

def check(user_input,a_account, b_account):
    if a_account>b_account:
        return user_input=='a'
    else :
        return user_input=="b"


print(art.logo)


compare1=choice()
compare2=choice()


score = 0
game_is_on=True


while game_is_on:

    compare1=compare2
    if compare1== compare2:
        compare2=choice()
    
    
    print(f"Compare A: {format_data(compare1)}.")
    print(art.vs)
    print(f"Against B: {format_data(compare2)}.")


    user_input=input("Who has more followers? Type 'A' or 'B': ").lower()


    a_account=compare1["follower_count"]
    b_account=compare2["follower_count"]

    is_correct= check(user_input,a_account,b_account)

    if is_correct:
        score+=1
        print(f"You are right your current score is {score}.")

    else:
        print(f"You are wrong your final score is {score}.")
        game_is_on=False
    

    




