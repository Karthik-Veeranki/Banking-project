# We need to integrate the SQL database with the python code so importing the necessay module
import mysql.connector as mc

# The admin should enter their database password but should not be visible to others, so using this module
import getpass

# to store the transaction date, we use datetime module
from datetime import date

# importing all the functionalities as modules
import addAccount
import modifyAccount
import deactivateAccount
import activateAccount
import details
import search
import transactions


# Various transaction options are available in this function
def transaction_options():
    while(True):
    
        print("\nTransaction options available:\n")
        print("1. Deposit")
        print("2. Withdrawl")
        print("3. Back to Main menu")
        
        ch = int(input("\nEnter your choice 1/2/3 : "))
        
        if(ch == 1):
            transactions.deposit_amount(sql_password)
        elif(ch == 2):
            transactions.withdraw_amount(sql_password)
        elif(ch == 3):
            break
        else:
            print("Please enter a valid choice")



# The main menu which runs in an infinite loop until you exit the application
def main_menu():
    while(True):
        print("\n#########################################################################\n")
        print("Main Menu")
        print("\n1. Add Account")
        print("2. Modify Account")
        print("3. Deactivate account")
        print("4. Activate account")
        print("5. Get Account Details")
        print("6. Search menu")
        print("7. Transaction Menu")
        print("8. Close the application")
        
        ch = int(input("\nPlease enter your choice (1/2/3/4/5/6/7/8): "))
        
        if(ch == 1):
            addAccount.add_account(sql_password)
        elif(ch == 2):
            modifyAccount.modify_account(sql_password)
        elif(ch == 3):
            deactivateAccount.deactivate_account(sql_password)
        elif(ch == 4):
            activateAccount.activate_account(sql_password)
        elif(ch == 5):
            details.fetch_account_details(sql_password)
        elif(ch == 6):
            search.search(sql_password)
        elif(ch == 7):
            transaction_options()
        elif(ch == 8):
            break




# Taking the password as input from user
sql_password = getpass.getpass("Please enter your Database password: ")
main_menu()
