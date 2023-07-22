# We need to integrate the SQL database with the python code so importing the necessay module
import mysql.connector as mc

# The admin should enter their database password but should not be visible to others, so using this module
import getpass

# to store the transaction date, we use datetime module
from datetime import date

# If the account holder wants to deactivate their account, we call this function
def deactivate_account(sql_password):
    connection = mc.connect(host = 'localhost', database = 'bankproject', user = 'root', password = sql_password)
    cursor = connection.cursor()
    
    AccNo = int(input("Enter Account Number: "))
    sql_statement_1 = "UPDATE Customer SET status = 'close' WHERE AccNo = '" + str(AccNo) + "';"
    #print(sql_statement_1)
    
    cursor.execute(sql_statement_1)
    
    sql_statement_2 = "COMMIT;"
    cursor.execute(sql_statement_2)
    print("\nAccount deactivated successfully !!")
    
    connection.close()


