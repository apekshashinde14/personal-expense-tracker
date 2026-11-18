from datetime import datetime
from database import con, cur

def add_expense():
    while True:
        title = input("Enter Expense Title: ").strip()
        if title:
            break
        else:
            print("Expense title cannot be empty!")
    while True:
        category = input("Enter Category: ").strip()
        if category:
            break
        else:
            print("Category cannot be empty!")
    while True:
        try:
            amount=float(input("Enter Amount: "))
            if amount <= 0 :
                print("Amount must be greater than zero!")
            else :
                break
        except ValueError:
            print("Please enter a valid numeric amount!")

    while True:
        try:
            date = input("Enter a date (DD/MM/YYYY): ").strip()
            date = datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date! Please enter in DD/MM/YYYY format.")
    cur.execute(
    "INSERT INTO expenses (title, category, amount, expense_date) VALUES (%s, %s, %s, %s)",
    (title, category, amount, date)
    )

    con.commit()
    print("Expense Added Successfully!!")

def view_expense():
    cur.execute("SELECT * FROM expenses")
    records = cur.fetchall()

    if not records:
        print("No Records Available!")
    else:
        print("Your Expenses Are: ")
        for item in records:
            print(f'Expense id = {item[0]}')
            print(f'Expense Title = {item[1]}')
            print(f'Expense Category = {item[2]}')
            print(f'Expense Amount = {item[3]}')
            print(f'Expense Date = {item[4]}')
            print("-" * 30)
            

def search_expense():
        title = input("Enter Title of Expense to Search : ")
        cur.execute("select * from expenses where title=%s",(title,))
        records = cur.fetchall()
        if not records:
                print("Expense Not Found!!")
        else :
            for item in records:
                    print(f'Expense id = {item[0]}')
                    print(f'Expense Title = {item[1]}')
                    print(f'Expense Category = {item[2]}')
                    print(f'Expense Amount = {item[3]}')
                    print(f'Expense Date = {item[4]}')
                    print("-" * 30)
        
            

def update_expense():
    id=int(input("Enter Id to update: "))
    cur.execute("SELECT * FROM expenses WHERE expense_id = %s", (id,))
    record = cur.fetchone()
    if not record :
        print("Expense Id not Found!!")
    else:
        while True:
            try:
                amount=float(input("Enter Amount: "))
                if amount <= 0 :
                    print("Amount must be greater than zero!")
                else :
                    break
            except ValueError:
                print("Please enter a valid numeric amount!")
        
        cur.execute(
        "UPDATE expenses SET amount = %s WHERE expense_id = %s",
        (amount, id))

        con.commit()
        print("Expense Updated Successfully!!")

def delete_expense():
    id=int(input("Enter Id to Delete: "))
    cur.execute("SELECT * FROM expenses WHERE expense_id = %s", (id,))
    record = cur.fetchone()
    if not record:
        print("Expense Id Not Found!!")
    else :
        cur.execute("DELETE FROM expenses WHERE expense_id = %s",(id,))
        con.commit()
        print("Expense Deleted Successfully!!")
        
def expense_summary():
    cur.execute("SELECT COUNT(*) FROM expenses")
    count = cur.fetchone()[0]

    print("======Expense Summary======")
    cur.execute("select sum(amount), count(*),avg(amount), max(amount), min(amount) from expenses")
    result=cur.fetchone()
    if result[1] == 0:
        print("No Expenses Available!")
        return
    print(f'Total Expenses = {result[0]}')
    print(f'Number of Expenses = {result[1]}')
    print(f'Average of Expenses = {result[2]}')
    print(f'Highest Expense : {result[3]}')
    print(f'Lowest Expense = {result[4]}')