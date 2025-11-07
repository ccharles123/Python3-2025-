import csv

monthly_sales = {}

with open('monthly_sales.csv', mode='r', encoding='utf-8') as file:  # <- guion bajo
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)
