import psycopg2

conn = psycopg2.connect(
    host="db",
    database="mydatabase",
    user="user",
    password="password"
)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, name VARCHAR(50), age INT);")

cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("John", 28))
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Anna", 24))
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Mike", 35))

conn.commit()

cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
