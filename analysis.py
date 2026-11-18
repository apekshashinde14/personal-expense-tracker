
import pandas as pd
import matplotlib.pyplot as plt

from database import con, cur


# 1. Fetch Data from MySQL Database

cur.execute("SELECT * FROM expenses")
records = cur.fetchall()


# 2. Convert Data into Pandas DataFrame

df = pd.DataFrame(records, columns=[
    'Expense_ID',
    'Title',
    'Category',
    'Amount',
    'Date'
])


# 3. Clean and Organize Category Data

df['Category'] = df['Category'].str.strip().str.title()


# 4. Category-wise Spending Analysis

total_spending = df.groupby('Category')['Amount'].sum()

highest_category = total_spending.idxmax()
highest_category_amount = total_spending.max()

print("\n----- Category-wise Spending -----")
print(total_spending)
print("Top Spending Category:", highest_category)
print("Amount Spent:", highest_category_amount)


# 5. Monthly Expense Analysis

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

monthly_spending = df.groupby(['Year', 'Month'])['Amount'].sum()
print("\n----- Monthly Spending -----")
print(monthly_spending)

highest_month = monthly_spending.idxmax()

year = highest_month[0]
month = highest_month[1]

month_name = pd.to_datetime(
    f'{year}-{month}-01'
).strftime('%B')

# 6. Overall Expense Summary

total_amount = df['Amount'].sum()
average_expense = df['Amount'].mean()
highest = df['Amount'].max()
lowest = df['Amount'].min()

print("\n" + "=" * 45)
print("          PERSONAL EXPENSE DASHBOARD")
print("=" * 45)
print("\n      FINANCIAL OVERVIEW")
print("-" * 45)
print(f"Total Spending       : ₹{float(total_amount):.2f}")
print(f"Average Expense      : ₹{float(average_expense):.2f}")
print(f"Highest Expense      : ₹{float(highest):.2f}")
print(f"Lowest Expense       : ₹{float(lowest):.2f}")

print("\n      TOP SPENDING CATEGORY")
print("-" * 45)
print(f"Category : {highest_category}")
print(f"Amount   : ₹{float(highest_category_amount):.2f}")

print("\n      MONTHLY OVERVIEW")
print("-" * 45)
print(f"Highest Spending Month : {month_name} {year}")

# 7. Category-wise Spending Chart

plt.figure(figsize=(8, 5))

bars = plt.bar(total_spending.index, total_spending.values)

plt.bar_label(bars, fmt='₹%.0f', padding=3)

plt.title("Total Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount (₹)")

# 8. Category-wise Spending Pie Chart

plt.figure(figsize=(7, 7))

plt.pie(
    total_spending.values.astype(float),
    labels=total_spending.index,
    autopct=lambda p: f'{p:.1f}%\n₹{p * float(total_spending.sum()) / 100:.0f}'
)

plt.title("Category-wise Expense Distribution")

# 9. Monthly Expense Chart

plt.figure(figsize=(8, 5))


monthly_labels = [
    pd.to_datetime(f'{year}-{month}-01').strftime('%B %Y')
    for year, month in monthly_spending.index
]
plt.bar(monthly_labels, monthly_spending.values)
plt.title("Monthly Expense Analysis")
plt.xlabel("Month")
plt.ylabel("Amount (₹)")


# 10. Display Charts

plt.show()
