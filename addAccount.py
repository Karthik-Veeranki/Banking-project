# We need to integrate the SQL database with the python code so importing the necessay module
import mysql.connector as mc

# The admin should enter their database password but should not be visible to others, so using this module
import getpass

# to store the transaction date, we use datetime module
from datetime import date


# This function is to add a new account by taking necessary information from the user
def add_account(sql_password):
    connection = mc.connect(host = 'localhost', database = 'bankproject', user = 'root', password = sql_password)
    cursor = connection.cursor()
    
    name = input("Enter the name of Account holder: ")
    address = input("Enter the Address of Account holder: ")
    email = input("Enter the email Id of Account holder: ")
    phoneNo = input("Enter the phone number of Account holder: ")
    aadhar = input("Enter the 12 digit Aadhar number of Account holder: ")
    account_type = input("Enter the type of account (Current/Savings): ")
    balance = input("Enter the opening balance amount: ")
    
    sql_statement_1 = "INSERT INTO Customer (Name, Address, email, phoneNo, AadharNo, AccType, status, balance) VALUES('" + name + "', '" + address + "', '" + email + "', '" + phoneNo + "', '" + aadhar + "', '" + account_type + "', 'active', " + balance + ");"
    #print(sql_statement)
    cursor.execute(sql_statement_1)
    
    sql_statement_2 = "COMMIT;"
    cursor.execute(sql_statement_2)
    
    print("\nAccount added successfully!!")
    
    connection.close()

    