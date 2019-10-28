import psycopg2
import csv
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

with open("user_accounts.csv", "r") as f:
    next(f)  # skip header
    reader = csv.reader(f)
    for row in reader:
        cur.execute("insert into users values (%s,%s,%s,%s);", row)