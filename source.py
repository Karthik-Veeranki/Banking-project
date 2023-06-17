# We need to integrate the SQL database with the python code so importing the necessay module
import mysql.connector as mc

# The admin should enter their database password but should not be visible to others, so using this module
import getpass

# to store the transaction date, we use datetime module
from datetime import date


# This function is to add a new account by taking necessary information from the user
def add_account():
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




# If the account holder wants to change any of his/her information, we call this function
def modify_account():
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





# If the account holder wants to deactivate their account, we call this function
def deactivate_account():
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




# If the account holder wants to activate their account, we call this function
def activate_account():
    connection = mc.connect(host = 'localhost', database = 'bankproject', user = 'root', password = sql_password)
    cursor = connection.cursor()
    
    
    AccNo = int(input("Enter Account Number: "))
    sql_statement_1 = "UPDATE Customer SET status = 'active' WHERE AccNo = '" + str(AccNo) + "';"
    #print(sql_statement_1)
    
    cursor.execute(sql_statement_1)
    
    sql_statement_2 = "COMMIT;"
    cursor.execute(sql_statement_2)
    print("\nAccount activated successfully !!")
    
    connection.close()





# This function gives the total details of Account Number entered.
def fetch_account_details():
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
    
    
    


# This function is used to search for the information based on user's input for any field
def search():
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







# To check whether the account is active or not, we call this function
def account_status(AccNo):
    connection = mc.connect(host = 'localhost', database = 'bankproject', user = 'root', password = sql_password)
    cursor = connection.cursor()
    
    sql_statement = "SELECT status,balance FROM Customer WHERE AccNo = '" + str(AccNo) + "';"
    cursor.execute(sql_statement)  # This method iterates over the rows of table
    result = cursor.fetchone()
    
    connection.close()
    return result


    
# If the user wants to deposit money into their account, we call this function
def deposit_amount():
    connection = mc.connect(host = 'localhost', database = 'bankproject', user = 'root', password = sql_password)
    cursor = connection.cursor()
    
    AccNo = input("Enter the Account Number: ")
    amount = input("Enter the amount to be deposited: ")
    
    
    current_date = date.today()     # To store the date of deposit
    
    # Once the user enters the account number, we need to check if the account is active or not
    sql_statement = "SELECT `status` FROM `Customer` WHERE `AccNo` = " + AccNo + ";"
    
    current_status = account_status(AccNo)
    
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
def withdraw_amount():
    connection = mc.connect(host = 'localhost', database = 'bankproject', user = 'root', password = sql_password)
    cursor = connection.cursor()
    
    AccNo = input("Enter the Account Number: ")
    amount = input("Enter the amount of withdrawl: ")
    
    current_date = date.today()     # To store the date of deposit
    
    # Once the user enters the account number, we need to check if the account is active or not
    current_status = account_status(AccNo)
    
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



# Various transaction options are available in this function
def transaction_options():
    while(True):
    
        print("\nTransaction options available:\n")
        print("1. Deposit")
        print("2. Withdrawl")
        print("3. Back to Main menu")
        
        ch = int(input("\nEnter your choice 1/2/3 : "))
        
        if(ch == 1):
            deposit_amount()
        elif(ch == 2):
            withdraw_amount()
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
            add_account()
        elif(ch == 2):
            modify_account()
        elif(ch == 3):
            deactivate_account()
        elif(ch == 4):
            activate_account()
        elif(ch == 5):
            fetch_account_details()
        elif(ch == 6):
            search()
        elif(ch == 7):
            transaction_options()
        elif(ch == 8):
            break




# Taking the password as input from user
sql_password = getpass.getpass("Please enter your Database password: ")
main_menu()