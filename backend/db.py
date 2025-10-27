import psycopg2
from psycopg2.extras import RealDictCursor

DB_DSN = "dbname=client_user_db user=postgres password=marti123 host=localhost port=5432"

def get_connection():
    """
    Creates a connection to the database.
    """
    return psycopg2.connect(DB_DSN)

def create_user(email, first_name, last_name, password_hash):
    """
    Creates a new user with the given email, first name and last name.
    :return: new user.
    """
    curr_command = """
        INSERT INTO users (email, first_name, last_name, password_hash)
        VALUES (%s, %s, %s, %s) RETURNING id
        """
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(curr_command, (email, first_name, last_name, password_hash))
            return cur.fetchone()["id"]

def get_user_by_email(email):
    """
    Gets a user by email.
    :return: user.
    """
    curr_command = "SELECT * FROM users WHERE email = %s"
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(curr_command, (email,))
            return cur.fetchone()

def update_user(email, first_name, last_name, password_hash):
    """
    Updates a user with the given email, first name and last name.
    """
    curr_command = """
    UPDATE users
    SET first_name = %s, last_name = %s, password_hash = %s
    WHERE email = %s
    """
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(curr_command,(first_name, last_name, password_hash, email))
            conn.commit()