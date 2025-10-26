import psycopg2
from psycopg2.extras import RealDictCursor

DB_DSN = "dbname=client_user_db user=postgres password=marti123 host=localhost port=5432"

def get_connection():
    return psycopg2.connect(DB_DSN)

def create_user(email, first_name, last_name, password_hash):
    curr_command = """
        INSERT INTO users (email, first_name, last_name, password_hash)
        VALUES (%s, %s, %s, %s) RETURNING id
        """
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(curr_command, (email, first_name, last_name, password_hash))
            return cur.fetchone()["id"]

def get_user_by_email(email):
    curr_command = "SELECT * FROM users WHERE email = %s"
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(curr_command, (email,))
            return cur.fetchone()

def update_user(email, first_name, last_name, password_hash):
    curr_command = """
    UPDATE users
    SET first_name = %s, last_name = %s, password_hash = %s
    WHERE email = %s
    """
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(curr_command,(first_name, last_name, password_hash, email))
            conn.commit()