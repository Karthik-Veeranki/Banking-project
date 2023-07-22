# We need to integrate the SQL database with the python code so importing the necessay module
import mysql.connector as mc

# The admin should enter their database password but should not be visible to others, so using this module
import getpass

# to store the transaction date, we use datetime module
from datetime import date

# This function is used to search for the information based on user's input for any field
def search(sql_password):
    connection = mc.connect(host = 'localhost', database = 'bankproject', user = 'root', password = sql_password)
    cursor = connection.cursor()
    
    while(True):
        print("\nSearch options:\n")
        print("1. Account Number")
        print("2. Name")
        print("3. Address")
        print("4. Email Id")
        print("5. Phone number")
        print("6. Aadhar Card")
        print("7. Back to Main menu")
        
        ch = int(input("Enter your choice 1/2/3/4/5/6/7 : "))
        
        field_name = ""
        
        if(ch == 1):
            field_name = "AccNo"
        elif(ch == 2):
            field_name = "Name"
        elif(ch == 3):
            field_name = "Address"
        elif(ch == 4):
            field_name = "email"
        elif(ch == 5):
            field_name = "phoneNo"
        elif(ch == 6):
            field_name = "AadharNo"
        elif(ch == 7):
            break
        else:
            print("Please enter a valid choice")
        
        
        field_value = input("Enter {}: ".format(field_name))
        
        if(field_name == "AccNo"):  # Account number is unique, so only one exists if present
            sql_statement = "SELECT * FROM Customer WHERE AccNo = '" + field_value + "';"
        else:       # Remaining may be duplicate, so we search using LIKE
            sql_statement = "SELECT * FROM Customer WHERE " + field_name + " LIKE '%" + field_value + "%';"
        
        cursor.execute(sql_statement)
        
        result = cursor.fetchall()      # stores all the rows that are output of above sql statement. Now, result is a list of tuples
        
        print("\nSearch result for {} {} is as follows: ".format(field_name, field_value))
        
        print("#########################################################################")
        
        print("AccNo     Name        Address       email            phoneNo         Aadhar          Acctype         status          balance")
        for i in range(len(result)):
            print("{}       {}      {}      {}      {}      {}      {}      {}      {}".format(result[i][0], result[i][1], result[i][2], result[i][3], result[i][4], result[i][5], result[i][6], result[i][7], result[i][8]))
        
        if(len(result) == 0):
            print("No such record exists")
            
        print("#########################################################################")

    connection.close()



