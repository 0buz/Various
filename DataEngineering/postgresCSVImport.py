import psycopg2
import csv
import os
from datetime import datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evolution.settings')
conn = psycopg2.connect("dbname=jobmarket user=pgrole host=localhost password=rpython")
cur = conn.cursor()
#
# cur.execute("select * from jobmarket_job limit 100;")
# res = cur.fetchall()
#
# for item in res:
#     print(item)

with open("/home/adrian/all/evolution/evolution/data/preprocessed/test_raw20191209.csv", "r") as f:
    next(f)  # skip header
    reader = csv.reader(f)
    for row in reader:
        a = datetime.strptime(row[-1], '%d/%m/%Y %H:%M:%S')
        created_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       # print((row[:-1]+[a.strftime('%Y-%m-%d %H:%M:%S'),created_date,'2']))
        cur.execute("INSERT INTO jobmarket_job(title, description, type, location, duration, start_date, rate, recruiter, posted_date,created_date, owner_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
                    (row[:-1]+[a.strftime('%Y-%m-%d %H:%M:%S'),created_date,'2']))
        print("inserted")
conn.commit()

cur.execute(
    """COPY jobmarket_job(title, type, location, duration, start_date, rate, recruiter, posted_date, description) 
    FROM '/home/adrian/all/evolution/evolution/data/preprocessed/test_raw20191209.csv' WITH (FORMAT csv);"""
)

conn.close()


a = datetime.datetime.strptime('my date', "%b %d %Y %H:%M")

cur.execute('INSERT INTO myTable (Date) VALUES(%s)', (a.strftime('%Y-%m-%d %H:%M:%S'),))
#cur.execute("INSERT INTO sms_log(member_id, recipient, message, status) VALUES (%s,%s,%s,%s);", (row[0],row[1],row[2],"Success"))