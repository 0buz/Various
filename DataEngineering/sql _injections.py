import timeit

import datetime

xx=datetime.datetime.now()

def get_email(name):
    import psycopg2
    conn = psycopg2.connect("dbname=dq user=dq")
    cur = conn.cursor()
    # create the query string using the format function
    query_string = "SELECT email FROM users WHERE name = '" + name + "';"
    # execute the query
    cur.execute(query_string)
    res = cur.fetchall()
    conn.close()
    return res


# add you code below


all_emails = get_email(
    "John Doe' OR 1 = 1;--")  # using this string as parameter will return ALL emails, not only that user's

print(get_email(
    "Larry Cain' UNION SELECT address FROM users WHERE name = 'Larry Cain"))  # With UNION command we can group together
# the result of two SQL queries as long as they both result in the same number of columns with matching data types.


# WORKAROUND: pass name as a second argument
def get_email_fixed(name):
   import psycopg2
   conn = psycopg2.connect("dbname=dq user=dq")
   cur = conn.cursor()
   # fix the line below
   cur.execute("SELECT email FROM users WHERE name = %s;", (name,))  # <<<<<<<<<<<<<<<<
   res = cur.fetchall()
   conn.close()
   return res


#====================== PREPARE statements  ===================================================================
""" PREPARE statements are another way of avoiding SQL injections.
PREPARE statements are only visible using the cursor from the connection with which it was created."""

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("""
    PREPARE insert_user(integer, text, text, text) AS
        INSERT INTO users VALUES ($1, $2, $3, $4);
""")
cur.execute("""
    EXECUTE insert_user($s, $s, $s, $s);
""", (10002, 'bob@dataquest.io', 'Bob', '101 Fake Street'))



# function that inserts all users using a prepared statement
def prepared_insert():
    conn = psycopg2.connect("dbname=dq user=dq")
    cur = conn.cursor()
    cur.execute("""
        PREPARE insert_user(integer, text, text, text) AS
        INSERT INTO users VALUES ($1, $2, $3, $4)
    """)
    for user in users:
        cur.execute("EXECUTE insert_user(%s, %s, %s, %s)", user)

# function that inserts all users using a new INSERT query for each user
def regular_insert():
    conn = psycopg2.connect("dbname=dq user=dq")
    cur = conn.cursor()
    for user in users:
        cur.execute("""
            INSERT INTO users VALUES (%s, %s, %s, %s)
        """, user)
    conn.close()

# ==========  See execution time comparison below   =====================
runtime_prepare = timeit.timeit(prepared_insert, number=1)
runtime_regular = timeit.timeit(regular_insert, number=1)

#===============================================================================================================



