# https://docs.python.org/3/tutorial/floatingpoint.html         --floatingpoint arithmetic
#method 1 
def total_bill_tip_split_calc():  
    print("Welcome to tip calculator")

    total_bill=int(input("What is the total bill? "))
    tip= int(input("How much tip would you like to give? 10, 12 or 15 ? "))
    peps= int(input("How many people to split the bill? "))

    def total_bill_calculation(total_bill, tip):
        total_final_bill=total_bill*(1+(tip/100))
        print(type(tip/100))
        return total_final_bill


        
    a=total_bill_calculation(total_bill, tip)


    def split(a,peps):
        split=round((a/peps),2)
        print(f"Each person needs to pay {split} $ ")

    split(a,peps)


if __name__== "__main__":
    total_bill_tip_split_calc()


