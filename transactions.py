# We need to integrate the SQL database with the python code so importing the necessay module
import mysql.connector as mc

# The admin should enter their database password but should not be visible to others, so using this module
import getpass

# to store the transaction date, we use datetime module
from datetime import date


# To check whether the account is active or not, we call this function
def account_status(AccNo, sql_password):
    connection = mc.connect(host = 'localhost', database = 'bankproject', user = 'root', password = sql_password)
    cursor = connection.cursor()
    
    sql_statement = "SELECT status,balance FROM Customer WHERE AccNo = '" + str(AccNo) + "';"
    cursor.execute(sql_statement)  # This method iterates over the rows of table
    result = cursor.fetchone()
    
    connection.close()
    return result


    
# If the user wants to deposit money into their account, we call this function
def deposit_amount(sql_password):
    connection = mc.connect(host = 'localhost', database = 'bankproject', user = 'root', password = sql_password)
    cursor = connection.cursor()
    
    AccNo = input("Enter the Account Number: ")
    amount = input("Enter the amount to be deposited: ")
    
    
    current_date = date.today()     # To store the date of deposit
    
    # Once the user enters the account number, we need to check if the account is active or not
    sql_statement = "SELECT `status` FROM `Customer` WHERE `AccNo` = " + AccNo + ";"
    
    current_status = account_status(AccNo, sql_password)
    
    #print(current_status)
    
    if(current_status[0] != 'active'):
        print("\nAccount doesn't exist")
    else:
        # first update the balance in the Customers table
        sql_statement_1 = "UPDATE Customer SET balance = balance + " + amount + " WHERE AccNo = '" + str(AccNo) + "' AND status = 'active';"
        
        # later make a new transaction record in the Transactions table
        sql_statement_2 = "INSERT INTO `Transaction`(`DateOfTrans`, `type`, `amount`, `AccNo`) VALUES('"+ str(current_date) + "', 'deposit', '" + str(amount) + "', '" + str(AccNo) + "');"
        
        # commit the changes done
        sql_statement_3 = "COMMIT;"
        cursor.execute(sql_statement_1)
        cursor.execute(sql_statement_2)
        cursor.execute(sql_statement_3)
        
        print("\nAmount deposited successfully")
        
    connection.close()
    


# If the user wants to withdraw money from their account, we call this function
def withdraw_amount(sql_password):
    connection = mc.connect(host = 'localhost', database = 'bankproject', user = 'root', password = sql_password)
    cursor = connection.cursor()
    
    AccNo = input("Enter the Account Number: ")
    amount = input("Enter the amount of withdrawl: ")
    
    current_date = date.today()     # To store the date of deposit
    
    # Once the user enters the account number, we need to check if the account is active or not
    current_status = account_status(AccNo, sql_password)
    
    if(current_status[0] != 'active'): 
        print("\nAccount doesn't exist")
    
    # We should check if there is sufficient balance available for withdrawl or not
    elif(float(current_status[1]) < float(amount)):
        print("\nInsuffient balance")
    
    else:
        sql_statement_1 = "UPDATE Customer SET balance = balance - " + amount + " WHERE AccNo = " + AccNo + " AND status = 'active';"
        sql_statement_2 = "INSERT INTO `Transaction`(`DateOfTrans`, `type`, `amount`, `AccNo`) VALUES('" + str(current_date) + "', 'withdraw', " + amount + ", " + AccNo + ");"
        sql_statement_3 = "COMMIT;"
        
        cursor.execute(sql_statement_1)
        cursor.execute(sql_statement_2)
        cursor.execute(sql_statement_3)
        
        print("\nAmount withdrawl successful")
    
    connection.close()


