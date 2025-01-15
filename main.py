import json
import mysql.connector as mysql


# Load JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database'
)
cursor = conn.cursor()

# Insert data into MySQL table
for record in data:
    cursor.execute(
        "INSERT INTO users (id, name, email) VALUES (%s, %s, %s)",
        (record['id'], record['name'], record['email'])
    )

# Commit and close connection
conn.commit()
cursor.close()
conn.close()

print("Data inserted into MySQL table successfully.")