print("Welcome to the secret auction program")

bid_list={}

bidding=True 
while bidding:
    a=input("What is your name? ")
    b=int(input("How much do you want to bid $"))
    bid_list[a]=b
    q=input("Do you have more bidders yes or no?").lower()
    
    if q=='no':
        # METHOD 1
        # s=""
        # max=0
        # for i in bid_list:
        #     if bid_list[i]>max:
        #         max=bid_list[i]
        #         s=i
        # print(f"The highest bidder is {s} with amount {max}")

        # METHOD 2
        bidding=False
        a =max(bid_list,key=bid_list.get)
        print(f"The highest bidder is {a} with amount {bid_list[a]}")
        
    else:
        print("\n"*20)
            
        