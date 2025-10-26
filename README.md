# Client-Server User Management App

## Technologies Used
- **Python 3.13** – main programming language for the backend scripts  
- **HTML** – for frontend templates  
- **PostgreSQL** – database for storing user data (registration, login, profile updates)  
- **psycopg2** – for connecting Python code with PostgreSQL  
- **http.server** – basic HTTP server integration  
- **unittest** – testing the functionality of the code  

## Functionalities and Implementation

### Registration
- User fills out a form with **email, first name, last name, password, and captcha**  
- Input data is validated using **regex**:  
  - Email must contain `@`  
  - Password must be at least 8 characters, contain at least one uppercase letter and one number  
- Password is **hashed using SHA256** before storing in PostgreSQL (`users` table)  

### Login
- Checks if the email exists in the database  
- Password entered by the user is verified against the stored **hashed password**  

### Profile
- Users can update their **first name, last name, and password**  
- Email is **not editable**  
- Password changes are hashed and validated again  

### Captcha
- Random code generated with **uppercase letters and numbers**  
- Ensures the user enters the correct captcha  

### Logout
- Displays a **static HTML confirmation page**  

## Ready-Made Functions / Modules Used
- **Python modules**:  
  - `re` – for regex validation  
  - `hashlib` – securely hash passwords  
  - `string` – for generating captcha symbols  
  - `random` – to generate random captcha codes  

- **Auth functions**:  
  - `is_valid_email(email)` – checks email validity  
  - `is_valid_name(name)` – checks name validity  
  - `is_valid_password(password)` – validates password strength  
  - `hash_password(password)` – hashes passwords using SHA256  
  - `verify_password(password, hashed_password)` – verifies a password against its hash  
  - `create_captcha(length=6)` – generates random captcha text  

- **Database functions**:  
  - `create_user(email, first_name, last_name, password_hash)` – adds a new user  
  - `get_user_by_email(email)` – retrieves user information by email  
  - `update_user(email, first_name, last_name, password_hash)` – updates user information  

## Project Files

