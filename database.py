import mysql.connector
import os

db_password = os.getenv("DB_PASSWORD")

if not db_password:
    print("Database password not found!")
    raise SystemExit
try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password=db_password,
        database="expense_tracker"
    )

    cur = con.cursor()
    print("Database Connected Successfully!")

except mysql.connector.Error as err:
    print("Database connection failed:", err)
    raise SystemExit