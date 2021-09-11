# Use only lowercase letters for variable names in tables(except for abbreviations)
# Use only UPPERCASE letters for table names
# Use same variable names for same thing from different tables


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
    joined_date DATE DEFAULT GETDATE(),
    username varchar(16) NOT NULL References LOGIN(username),
    UID BIGINT NOT NULL Unique check(100000000000 <= UID <= 999999999999),
    UID_photo BLOB NOT NULL,
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
    subscription_id VARCHAR(100) PRIMARY KEY,
    subscription_amount INT(10),
    max_books INT(10)
);
  
  
 
 
# Book details
 
CREATE TABLE BOOK (
    book_id VARCHAR(100) UNIQUE,
    title CHAR(100),
    auther CHAR(100),
    publication VARCHAR(100),
    edition VARCHAR(100),
    no_of_copies INT(10),
    date_of_purchase DATE,
    no_of_pages INT(100),
    prices INT(10),
    type CHAR(100),
    genre VARCHAR(100), 
    age_rating INT(5),
    current_book_holder CHAR(100), 
    PRIMARY KEY(book_id)
);
 
 
 
 
# Fine_table
 
CREATE TABLE FINE(
    user_library_id VARCHAR(100),
    book_id VARCHAR(100),
    fine_amount INT(10),
    paid ENUM('Yes','No'),
    paid_date DATE, 
    FOREIGN KEY(user_library_id) REFERENCES USER_LIBRARY_DATA(library_id)
    FOREIGN KEY(book_id) REFERENCES BOOK(book_id)
);
       
  
  
# Book_History

CREATE TABLE BOOK_HISTORY(
    current_book_Holder_id VARCHAR(100),
    book_id VARCHAR(100),
    book_issued DATE,
    book_returned DATE,
    fine_with_book INT(10)
);



# table_about review:
CREATE TABLE BOOK_REVIEW(
    book_id REFERENCES BOOK(book_id),
    user_id references user(library_id),
    comment varchar(1000) ,
    rating int not null check 1<=rating <=5,
    like_dislike bool 
 );
 
  
   





