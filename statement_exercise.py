def atm_machine():
    current_balance = 10000
    min_withdrawal = 500
    max_withdrawal = 5000
    move_on = True 
  
    while move_on:
        print("Welcome to the ATM machine")

        choice = input("Do you want to withdraw money? (yes/no): ")

        if choice == "no":
            print("Thank you for using the ATM")
            break

        elif choice == "yes":
            withdrawal_amount = int( input("Inter the amount you want to withdrawal: "))

            if withdrawal_amount <min_withdrawal:
                print("This process can not be proceed because the withdrawal amount is below the min. amount ")

            elif withdrawal_amount > max_withdrawal:
                print("the withdrawal amount exceeds the maximum amount allowed")

            elif withdrawal_amount > current_balance:
                print("Your current balance is Insufficient for this transaction")

            else:
                current_balance -= withdrawal_amount
                print("Sucessful Transaction, your remaining balance is:", current_balance)

            

            if current_balance < 500:
                move_on = False
        print(current_balance)
    
atm_machine()
            






