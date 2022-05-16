
print("Welcome to the DeDI Bank")
user_pin = 12345
#user_pin = int(input({12345, 12346, 12347,}))
trials = 3
balance = 50000

while trials != 0:
    pin = int(input("Please enter your 5 digit PIN number: "))
    if pin != user_pin:
        trials -= 1
        print("Wrong PIN number, you have", trials, "trials left")
             
    else:
        user_choice = input("D: deposit, W: withdraw, B: balance  :   ")
        if user_choice == "D":
            user_deposit = int(input("Please enter the amount you want to deposit: "))
            total_balance = user_deposit + balance
            print(user_deposit, "$ have been deposited and your total balance is $", total_balance)
        
        if user_choice == "W":
            user_withdraw = int(input("Please enter the amount you want to withdraw: "))
            total_balance = user_withdraw - balance
            print(user_withdraw, "$ have been withdrawn from your account, current balance is $", total_balance) 
        
        if user_choice == "B":
            user_balance = balance
            print("Your balance is $", user_balance)  
        
    user_exit = input("Would you like to withdraw from your account? Y/N: ")
    if user_exit == "N":
        print("Thank you for using the DeDI Bank")
        break
    else:
        continue
    
      
      
