import math


while True: # Creates a loop for the program which user can leave by typing "exit"
    print(" ")
    print("Investment - to calculate the amount of interest  you'll earn on your investment")
    print("Bond - to calculate the amount you'll have to pay on a home loan\n") 

    invest_or_bond = input("Enter either 'Investment' or 'Bond' from the menu above to proceed or enter 'exit' to leave: ").lower() # Asks user for input for if they want to calculate bonds or investment

    if invest_or_bond == "exit":
    
        break # Breaks the loop if user inputs the word "exit"

    if invest_or_bond == "investment": # If the user inputs the word "investment" then the following code runs to receive the data required for calculations
        
        deposit_amount = float(input("Please enter the amount too deposit: "))
        int_rate = float(input("Please enter the interest rate: "))
        int_rate = int_rate / 100
        years_of_invest = int(input("How many years do you plan to invest: "))
        interest = input("Would you like simple or compound interest: ").lower()
        
        if interest == "simple": # If user inputs "simple" then the simple interest calculator continues
            
            total_simple = round(float(deposit_amount * (1 + int_rate * years_of_invest)), 2) # formula for simple interest
            print(f"You will have a return of {total_simple}")
        
        elif interest == "compound": # If user inputs "compound" then the compound calculator is used instead
        
            total_comp = round(float(deposit_amount * math.pow((1 + int_rate), years_of_invest)), 2) # formula for compound interest
            print(f"You will have a retun of {total_comp}")
            

    elif invest_or_bond == "bond": # If user inputs "bond" then the bond calculator is used
        
        house_value = float(input("Please enter the house value: ")) 
        int_rate = float(input("Please enter the interest rate: "))
        int_rate = int_rate / 100
        monthly_int_rate = int_rate / 12
        repayment_time = int(input("Please enter the amount of months for repayment: "))

        repayment = (monthly_int_rate * house_value) / (1 - (1 + monthly_int_rate) ** (-repayment_time)) # formula for bond repayment
        print(f"You will have to pay {round(repayment, 2)} per month")

    else:
        print("Error, please try again")




        




