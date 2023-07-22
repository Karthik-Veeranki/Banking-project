# We need to integrate the SQL database with the python code so importing the necessay module
import mysql.connector as mc

# The admin should enter their database password but should not be visible to others, so using this module
import getpass

# to store the transaction date, we use datetime module
from datetime import date

# This function gives the total details of Account Number entered.
def fetch_account_details(sql_password):
    AccNo = int(input("Enter the Account Number : "))
    connection = mc.connect(host = 'localhost', database = 'bankproject', user = 'root', password = sql_password)
    cursor = connection.cursor()
    
    sql_statement_1 = "SELECT * FROM Customer WHERE AccNo = " + str(AccNo) + ";"
    sql_statement_2 = "SELECT * FROM Transaction WHERE Transaction.AccNo = " + str(AccNo) + ";"
    
    cursor.execute(sql_statement_1)
    result = cursor.fetchone()      # Since Account number is unique, we find only one record.
    
    print("#########################################################################")
    print("Account Number   :   {}".format(result[0]))
    print("Holder Name      :   {}".format(result[1]))
    print("Address          :   {}".format(result[2]))
    print("email Id         :   {}".format(result[3]))
    print("Phone number     :   {}".format(result[4]))
    print("Aadhar Number    :   {}".format(result[5]))
    print("Account type     :   {}".format(result[6]))
    print("Account statuts  :   {}".format(result[7]))
    print("Balance          :   {}".format(result[8]))
    
    
    cursor.execute(sql_statement_2)
    result = cursor.fetchall()      # For a single account number, many transactions are possible, hence we use fetchall()
    
    print("\nTransaction history")
    print("TransactionId    Date        Type    Amount")
    for i in range(len(result)):
        print("{}               {}  {}  {}".format(result[i][0], result[i][1], result[i][2], result[i][3]))
    
    
    connection.close()
    
    
    
