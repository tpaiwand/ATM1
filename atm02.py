
print("Welcome to the Example Bank")
user_pin = 12345
accounts = {"ABC": 12345, "ABCD": 12346, "ABCDE": 12347}
trials = 3
balance = 50000
account_valid = False

while trials != 0:
    input_account_name = str(input("Please enter your name: "))
    if (input_account_name in accounts):
        account_valid = True
    else:
        print("No valid account found.")
        exit(1)
    input_pin = int(input("Please insert your 5 digit pin number!"))
    if input_pin != accounts [input_account_name]:
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
            total_balance = balance - user_withdraw
            print(user_withdraw, "$ have been withdrawn from your account, current balance is $", total_balance) 
        
        if user_choice == "B":
            user_balance = balance
            print("Your balance is $", user_balance)  
        
    user_exit = input("Would you like to withdraw from your account? Y/N: ")
    if user_exit == "N":
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
    else:
        print("Thank you for using the Example Bank")
        break
              
      
