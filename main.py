from expense import (
    add_expense,
    view_expense,
    search_expense,
    update_expense,
    delete_expense,
    expense_summary
)

from database import con, cur

while True:
    print("========Welcome to Expense Tracker System==========")
    print("\n1.Add Expense\n2.View All Expense\n3.Search Expense \n4.Update Expense\n5.Delete Expense\n6.View Expense Summary\n7.Exit")
    print()
    while True:
        try:
            choice = int(input("Enter your choice: "))

            if 1 <= choice <= 7:
                break
            else:
                print("Please enter a choice between 1 and 7!")

        except ValueError:
            print("Please enter a valid numeric choice!")
    if choice == 1 :
        add_expense()
    elif choice == 2:
        view_expense()
    elif choice == 3:
        search_expense()
    elif choice == 4:
       update_expense()
    elif choice == 5:
        delete_expense()
    elif choice == 6:
        expense_summary()
    elif choice == 7:
        print("Thank you for using expense tracker!!")
        cur.close()
        con.close()
        break
    
