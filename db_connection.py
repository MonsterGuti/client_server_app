import psycopg2

conn = psycopg2.connect("dbname=client_user_db user=postgres password=marti123 host=localhost port=5432")
cur = conn.cursor()
cur.execute("SELECT * FROM users;")

for row in cur.fetchall():
    print(row)

cur.close()
conn.close()
