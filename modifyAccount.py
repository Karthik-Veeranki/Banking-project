# We need to integrate the SQL database with the python code so importing the necessay module
import mysql.connector as mc

# The admin should enter their database password but should not be visible to others, so using this module
import getpass

# to store the transaction date, we use datetime module
from datetime import date

# If the account holder wants to change any of his/her information, we call this function
def modify_account(sql_password):
    connection = mc.connect(host = 'localhost', database = 'bankproject', user = 'root', password = sql_password)
    cursor = connection.cursor()
    AccNo = int(input("Enter account number: "))
    
    print("\nWhich field do you want to change?")
    print("1. Name")
    print("2. Address")
    print("3. email Id")
    print("4. Phone Number")
    
    ch = int(input("Enter your choice (1/2/3/4): "))
    
    field_name = ""
    
    if(ch == 1):
        field_name = "Name"
    elif(ch == 2):
        field_name = "Address"
    elif(ch == 3):
        field_name = "email"
    elif(ch == 4):
        field_name = "phoneNo"
    else:
        print("Please enter a valid choice !!")
    
    
    field_value = input("Enter the new {}: ".format(field_name))
    
    sql_statement_1 = "UPDATE Customer SET " + field_name + " = '" + field_value + "' WHERE AccNo = '" + str(AccNo) + "';"
    
    cursor.execute(sql_statement_1)
    #print(sql_statement_1)
    
    sql_statement_2 = "COMMIT;"
    cursor.execute(sql_statement_2)
    
    print("\nInformation updated successfully !!")
    
    connection.close()

    