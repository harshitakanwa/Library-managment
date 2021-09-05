CREATE DATABASE LIBRARY;
use LIBRARY;



# User Registration Details

CREATE TABLE USER (
    library_id int PRIMARY KEY AUTO_INCREMENT,
    full_name varchar(50) NOT NULL,
    mobile BIGINT(10) check(1000000000<=mobile<=9999999999),
    email varchar(300) NOT NULL,
    DOB DATE NOT NULL,
    gender char(1) NOT NULL check(gender="M" or gender="F"),
    joined_date DATE NOT NULL,
    username varchar(16) NOT NULL References LOGIN(username),
    UID BIGINT NOT NULL Unique check(100000000000 <= UID <= 999999999999),
    user_type varchar(5) NOT NULL   # User/Admin
    address varchar(200) NOT NULL,
    status varchar(50) NOT NULL
);



# Login details

CREATE TABLE LOGIN (
    username varchar(16) Unique PRIMARY KEY check(CHAR_LENGTH(username)>=8),
    password varchar(100) NOT NULL check(CHAR_LENGTH(password)>=8)
);



# User_Library_Data

CREATE TABLE USER_LIBRARY_DATA (
    library_id int PRIMARY KEY references USER(library_id),
    no_of_books INT(10),
    max_no_of_books INT(10),
    joined_on DATE DEFAULT GETDATE(),
    photo MEDIUMBLOB NOT NULL,
    admin CHAR(100),
    fine CHAR(100)
);



# Subscription details

CREATE TABLE SUBSCRIPTION (
    Subscription_ID VARCHAR(100) PRIMARY KEY,
    Subscription_Amount INT(10),
    Max_Books INT(10)
);
  
  
 
 
# Book details
 
CREATE TABLE BOOK (
    Book_ID VARCHAR(100) UNIQUE,
    Title CHAR(100),
    Auther CHAR(100),
    Publication VARCHAR(100),
    Edition VARCHAR(100),
    No_OF_Copies INT(10),
    Date_Of_Purchase DATE,
    No_Of_Pages INT(100),
    Prices INT(10),
    Type CHAR(100),
    Genere VARCHAR(100), 
    Age_rating INT(5),
    Current_Book_Holder CHAR(100), 
    PRIMARY KEY(Book_ID)
);
 
 
 
 
# Fine_table
 
CREATE TABLE Fine_table(
    User_Library_ID VARCHAR(100),
    Book_ID VARCHAR(100),
    Fine_Amount INT(10),
    Paid ENUM('Yes','No'),
    Paid_Date DATE, 
    FOREIGN KEY(User_Library_ID) REFERENCES User_Library_Data(Username)
    FOREIGN KEY(Book_ID) REFERENCES Book(Book_ID)
);
       
  
  
# Book_History

CREATE TABLE Book_History(
    Current_Book_Holder_ID VARCHAR(100),
    Book_Issued DATE,
    Book_Returned DATE,
    Fine_with_Book INT(10)
);









