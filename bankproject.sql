SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


CREATE DATABASE bankproject;
USE bankproject;

-- if the table already exists, we should delete it entirely
DROP TABLE IF EXISTS `Customer`;

-- now freshly create the table with required fields



CREATE TABLE IF NOT EXISTS `Customer`(
	`AccNo` INT(18) AUTO_INCREMENT PRIMARY KEY,		-- Account number has maximum 18 digits and has auto increment feature , 
													-- setting the Account number as primary key, so not duplicate values and NULL values allowed
	`Name` VARCHAR(30) DEFAULT NULL,				-- Name of the Customer, with default value NULL
	`Address` VARCHAR(30) DEFAULT NULL,				-- Address of the Customer, with default value NULL
	`email` VARCHAR(50) DEFAULT NULL,				-- email ID of the Customer, with default value NULL
	`phoneNo` VARCHAR(20) DEFAULT NULL,				-- phone number of the customer, can include the country code as well 
	`AadharNo` VARCHAR(20) DEFAULT NULL,			-- aadhar number of customer, standard 12 digit number

	`AccType` VARCHAR(10) DEFAULT NULL,				-- account type, savings or current
	`status` VARCHAR(10) DEFAULT NULL,				-- status of account, active or not
	`balance` FLOAT(13, 2) DEFAULT NULL				-- balance in the account, maximum of 13 digits with 2 decimal points allowed
		
									
);




-- Whenever the code is run, there are atleast two users by default having their account in the bank
INSERT INTO `Customer`(`AccNo`, `Name`, `Address`, `email`, `phoneNo`, `AadharNo`, `AccType`, `status`, `balance`) 
VALUES (1, 'Dhoni', 'MG Road, Delhi', 'mahi@gmail.com', '1234567890', '879654152368', 'Savings', 'active', 35000.00),
	   (2, 'Kohli', 'Magestic, Bengaluru', 'vkohli@gmail.com', '9632587014', '852147536985', 'Current', 'active', 62000.00);





DROP TABLE IF EXISTS `Transaction`;

CREATE TABLE IF NOT EXISTS `Transaction`(
	`trans_id` INT(10) AUTO_INCREMENT PRIMARY KEY,		-- Transaction id which is unique for every transaction
	`DateOfTrans` DATE DEFAULT NULL,					-- date of transaction 
	`type` VARCHAR(10) DEFAULT NULL,					-- type of transaction, deposit or withdraw
	`amount` FLOAT(13, 2) DEFAULT NULL,					-- amount of transfer
	`AccNo` INT(18) DEFAULT NULL						-- account number on which you are performing the transaction

);



INSERT INTO `Transaction`(`trans_id`, `DateOfTrans`, `type`, `amount`, `AccNo`) 
VALUES(1, '2023-05-12', 'deposit', 5000.00, 1),
	  (2, '2023-05-15', 'withdraw', 8000.00, 2);
	  