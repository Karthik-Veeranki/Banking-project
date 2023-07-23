# Banking application

This application integrates the MySQL database to store the account holders' information and Transaction history using CRUD operations with the Python programming using module mysql.connector.
This application provides several functionalities to a bank customer:
1. Add a new account
2. Modify the existing account
3. De-activating an account
4. Activating their account
5. Fetch the details of the account
6. Search for the account
7. Transactions options

These functionalities are implemented as seperate modules in the code to maintain readabilty and semantics.

    Add a new account : In this module, first we connect to the SQL database. 
                        After successfully connected with the database, we ask the user to enter the necessary information from them, which we feed into Customer table using query   statements (INSERT INTO) in SQL. 
                        Finally commit the changes in database and display success message to user.

    Modify the existing account : After connecting to the database, we ask the user which field to change and update the corresponding field using UPDATE query.                                       
                                  Finally commit the changes in database and display success message to user.

    De-activating an account : After connecting to the database, we ask the user to enter the unique account number. 
                               Then update the status of account to close for that entry using UPDATE and WHERE queries.

    Activating an account : After connecting to the database, we ask the user to enter the unique account number. 
                            Then update the status of account to active for that entry using UPDATE and WHERE queries.

    Fetch the details : Entering the account number, we fetch the entire row of that account number and display their details along with their Transaction history. 
                        This is done using SELECT and WHERE queiry statements.

    Search for the account : If we want to fetch the details of the customer using any of their information (not just Account number), this module fetches the information close to field value. 
                             We can search using Account Number/Name/Address/email/phoneNumber/AadharNo.

    Transactions options : This module provides two services - withdraw and deposit money. 
                            Withdraw will debit specific amount entered by the customer from an active account with sufficient balance.   
                            Deposit will credit specific amount into active account.

In the source.py file, we take the input of password of MySQL database, that is needed to connect to the database. This is passed as parameter to every function we call to connect to database. Later enter into an infinite loop that displayes all the functionalities to the customer. If they wish to exit the application, enter apprpriate option to break the loop and terminate the application.

At the database server level, we have two tables - Customer and Transaction. By default, there are two entries in both tables

Customer stores the following fields : Account Number, Name, Address, email, phone number, Aadhar Number, Account type, Account status, balance.
Account Number is the primary key and has an auto-increment property.

Transaction stores the following fields : transaction id, date of transaction, transaction type, amount transfered, account number.
Transaction id is the primary key and has an auto-increment property.

