Technologies I used in this project:
**python 3.13** - This is the main language I wrote the scripts - backend
**HTML** - for the frontend
**PostgreSQL** - used for the data base when the user wants to register, log out or change profile
**psycopg2** - for the connection between the code i wrote and data base
**http.server** - the integration of the server
**unittest** - testing the functionality of the code

Functionalities and implementation:captcha
**register**
The user fills out a form with email, first name, last name, password and captcha.
His data is checked by regex. The email must contain "@", the password must be at least 8 characters and contains capital letter and number.
His password is being hashed with SHA256 and saved in the PostgreSQL database (users table).
**login**
The email is written in the database.
The entered password is compared to the hashed one in the database that belongs to the given email address.
**profile**
The user could change his data excluding his email.
The password again is checked with the hashed one in the database.
**captcha**
A random code with uppercase letters and numbers is generated.
It is checked whether the entered code matches the generated one.
**logout**
Loads a static HTML confirmation page.

Used ready made functions/modules:
**re** - for regular expression and data validation
**hashlib** the module is used to securely convert passwords or other data into 64-character hexadecimal string hashes for safe storage and verification.
**string** - this helped me for generating a random captcha code - added all the letters and all the numbers from 0 to 9
**random** - this is for the random generator that creates the captcha code - a random string whixh consists capital letters and numbers - for the user when 
**is_valid_email(email)** – checks if the email is validbacke
**is_valid_name(name)** – checks if the name is valid
**is_valid_password(password)** – checks if the password is strong
**hash_password(password)** – hash the password
**verify_password(password, hashed_password)** – verify the password against the hash
**create_captcha(length=6)** – generates random text for the captcha
**create_user(email, first_name, last_name, password_hash)** – adds a new user
**get_user_by_email(email)** – returns information about a user by email
**update_user(email, first_name, last_name, password_hash)** – updates information about a user

Files in the project:
**backend --> auth --> utils.py** - Validation, hashing, and captcha functions
**backend --> db.py** - CRUD database operations (create_user, get_user_by_email, update_user)
**backend --> server.py** - Basic HTTP server – handles GET and POST requests
**frontend --> templates** - HTML templates for pages (register, login, profile, logout)
**tests/test_auth.py** --Unit tests for the auth functions
**tests/test_db.py** --> Unit tests for the database















