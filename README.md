<a href="https://jithendra1798.pythonanywhere.com/"><h1 align = "center">Generic Library Managment</h1></a>

## Members
||Name|Roll No|Email|
|---:|:---|:---:|:---|
|1.| Jithendra Puppala | 191CS237 | <jithendra.191cs237@nitk.edu.in> |
|2.| Vamshikrishna M | 191CS261 | <vamshikrishnam.191cs261@nitk.edu.in>|
|3.| Mahadev Hatti  | 191CS133 |<mahadev.191cs133@nitk.edu.in>|
|4.| Keerthana Patil | 191CS231 |<patilkeerthana.191cs231@nitk.edu.in>|
|5.| Harshita | 191CS120 |<harshita.191cs120@nitk.edu.in>|

## Roadmap of the Project
![Roadmap of Library Management project image](https://raw.githubusercontent.com/jithendra1798/SE-Project/main/assets/Library%20Roadmap.jpg)

## Project Description
* As the project name suggests automation in which the human input can be minimised and makes the work of librarian a lot easier and experience of user a lot simpler.
* This has some new features like requesting book from other students, buying books from catalogue, if available for sale and reviewing and rating books and feedback of experience etc.  
* We can also track the history of users (books user has taken before and now).  
* We can also track history of books (users who took the book previously and now).  
* It makes library user and librarian work very simpler and easier.  

## Project Design Flow
![Project Design Flow](https://github.com/jithendra1798/SE-Project/blob/main/assets/Project%20Design%20Flow.png)

## Project Requirements/Features

### 1. Admin
 * Add books
 * Confirm registration of user
 * Can see all user details
 * Remove/add users
 * Make others admin
 * Can see the books taken by user
 * Can track history of book (Users used)


### 2. User
> There are 3 types of users
 
|New registration|Active user|Old user|
|:---|:---|:---|
|Registration yet to approve|Registration Approved|User in break/due fine|
|Shows Registration Pending|Can Access completely|Limited access|

#### Active user features :
- Can lend max of 4 books.
- Request other user, if he needs a book taken by other user.
- Pays fine, if he lost the book or delays renewal of book.
- History of books he took.
- Can buy a book, if availabe to sale by another user or by library.
- Can generate and use the Library ID card in PDF
- Can give Feedback of experience while taking books

### 3. Other Features
- Automated emails to users, reminding for renewal of books
- Users can search books in the catalogue
- Lending/Taking books is of 3 categories
    - Take book from Library
    - Take book from other user
    - Buy book, if available for sale
- Automated emails on registration approval/banning/termination
- Automated generation of Library ID cards
- Different types of subscriptions for users

## Software Specifications
|Backend|Frontend|
|:---|:---|
|Django (Python)|HTML|
MySQL(Database)|CSS|
|   |JS|

## Non-Functional Requirements
- Scalability and reliability is taken care by django, as it is simple, highly scalable and flexible.
- Security of the sensitive data transmission of users is taken care by django.
- We designed the database with high data integrity.
- The performance of the application will be good with the optimised queries in MySQL.
- Maintainability and Manageability of the application will be good, as we are following the best Software principles.
- MySQL is capable enough to scale the project to even higher.
- The portability of the application is high, as we are using one of the most popular framework.




## Links and Documents
### 1. [Schema Diagram PDF](https://github.com/jithendra1798/SE-Project/blob/main/assets/Tables%20Schema1.pdf)
### 2. [Schema Diagram Document](https://docs.google.com/document/d/1f0tBZoOreObHvXWhmM2hPPdkngzHdIXYdW9x57JuSEk/edit)
### 3. [Schema variables Document](https://docs.google.com/document/d/1xRhhgMQ8qZG436_hzpF3xj-nXgE0rf1wI6bEavzY5KE/edit)
### 4. [Library Project Design Flow](https://whimsical.com/library-8khLqftvQHyXJhb3m7ecsL)
### 5. [Reference e-Library](https://www.edigitallibrary.com/)
### 6. [Embed MySQL in Python/Django](https://www.tutorialspoint.com/python_data_access/python_mysql_introduction.htm)
### 7. [Dynamic Search Field - Django](https://betterprogramming.pub/how-to-make-search-fields-dynamic-in-django-rest-framework-72922bfa1543)
### 8. [Dynamic Search Field 2 - Django](https://openfolder.sh/django-tutorial-as-you-type-search-with-ajax)
