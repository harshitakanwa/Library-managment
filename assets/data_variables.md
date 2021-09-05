## Add all the possible variables we have to store in the database.
## Anything you think we have to store in DataBase please add them here.
## We will prepare schema using these variables

1. User
    - Name
    - mobile
    - email
    - UID
    - Address
    - Photo
    - DOB
    - No.of Books
    - Joined on
    - Generate Library ID
    - username
    - password
    - status(Accept/Rejected/Banned)
    - Fine


2. Admin
    - All details as user
    - Previous admins


3. Book
    - Name
    - Author
    - No.of Pages
    - Type(Hardcover etc)
    - Genre
    - Age rating
    - Book history
         - User
         - Date taken
         - Date returned
         - Fine with the book
    - Current book holder

4. Other
    - Books for sale
        - Price
        - book owner
        - All book details as above
    - Access book database
    - Request book
        - Requestd user
        - Requesting user
        - Book ID
        - Secret Key
    - Library ID card

5. Registration types
    - Archived
    - New
    - Accepted
    - Rejected
