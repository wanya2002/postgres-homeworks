import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    port='5433',
    database='north',
    user='postgres',
    password='Power6789012345'
)

try:
    with conn:
        with conn.cursor() as cur:
            with open("north_data\customers_data.csv", encoding='utf-8') as r_file:
                file_reader = csv.DictReader(r_file, delimiter=",")
                for row in file_reader:
                    cur.execute("INSERT INTO customers VALUES(%s, %s, %s)",[row["customer_id"],row["company_name"],row["contact_name"]])
            with open("north_data\employees_data.csv", encoding='utf-8') as r_file:
                file_reader = csv.DictReader(r_file, delimiter=",")
                for row in file_reader:
                    cur.execute("INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)",[row["employee_id"],row["first_name"],row["last_name"],row["title"],row["birth_date"],row["notes"]])
            with open("north_data\orders_data.csv", encoding='utf-8') as r_file:
                file_reader = csv.DictReader(r_file, delimiter=",")
                for row in file_reader:
                    cur.execute("INSERT INTO orders VALUES(%s, %s, %s, %s, %s)",[row["order_id"],row["customer_id"],row["employee_id"],row["order_date"],row["ship_city"]])
finally:
    conn.close()




