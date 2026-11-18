import mysql.connector
import os

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="expense_tracker"
    )

    cur = con.cursor()
    print("Database Connected Successfully!")

except mysql.connector.Error as err:
    print("Database connection failed:", err)
    raise SystemExit