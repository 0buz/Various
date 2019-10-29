import psycopg2

conn = psycopg2.connect("dbname=test user=pgrole host=localhost password=rpython")

cur = conn.cursor()
cur.execute("select * from aprest_aprest;")



#A - loop through query results
for row in cur:
    print(row)

#or B - get the first row or a list (of tuples) with all rows
cur.execute("select * from users;")
one_result = cur.fetchone()
all_results = cur.fetchall()
some_results = cur.fetchmany(3)


#===========================  CREATE TABLE and ALTER TABLE examples    ===============================================
import psycopg2
conn = psycopg2.connect("user=dq dbname=dq")
cur = conn.cursor()
# triple double quotes to make the statement a bit more readable; single double quotes "" suffice otherwise
cur.execute("""
    CREATE TABLE employees(
        id integer PRIMARY KEY, 
        first_name text, 
        last_name text
    );
""")

cur.execute("ALTER table ign_reviews alter COLUMN id TYPE bigint;")
cur.execute("ALTER table ign_reviews alter COLUMN score TYPE DECIMAL(3,1);")
#=====================================================================================================================

# =============  Get table description with cursor.description  ======================================================
table_description = cur.description
for item in table_description:
    print(item)

colnames = [desc[0] for desc in cur.description]  #just column names
#=====================================================================================================================


# =============  pg_catalog.pg_type contains data type details  ======================================================
query="select * from pg_catalog.pg_type"
cur.execute(query)
all_results = cur.fetchall()

cur.execute("SELECT typname FROM pg_catalog.pg_type WHERE oid = 23;")
type_name_23 = cur.fetchone()[0]
print(type_name_23)

cur.execute("SELECT typname FROM pg_catalog.pg_type WHERE oid=25 or oid=700;")
type_name_25 = cur.fetchone()[0]
type_name_700 = cur.fetchone()[0]   # fetch the next row
all_results = cur.fetchall()
#=====================================================================================================================


# =============  Set datatype as ENUM i.e. a fixed list of values  ===================================================
cur.execute("""
    CREATE TYPE evaluation_enum AS ENUM (
    'Great',       'Mediocre', 'Bad', 
    'Good',        'Awful',    'Okay', 
    'Masterpiece', 'Amazing',  'Unbearable', 
    'Disaster',    'Painful');
""")

cur.execute("""ALTER TABLE ign_reviews
ALTER COLUMN score_phrase TYPE evaluation_enum
USING score_phrase::evaluation_enum;
""")
#=====================================================================================================================


# =============  INSERT examples  ====================================================================================

# == 1 Insert with tuple ======
cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s);", (1, "hello@dataquest.io", "John", "123, Fake Street"))

cur.execute("INSERT INTO foo VALUES (%s)", "bar")    # WRONG
cur.execute("INSERT INTO foo VALUES (%s)", ("bar"))  # WRONG
cur.execute("INSERT INTO foo VALUES (%s)", ("bar",)) # correct
cur.execute("INSERT INTO foo VALUES (%s)", ["bar"])  # correct
# translates to INSERT directly into dbe.g. insert into reviews(id, name, email, rating)  values (1, 'Ady', 'ady@email.com', 'Great');


# == 2 Insert with dictionary =====
row_values = {
    'identifier': 1,
    'mail': 'adam.smith@dataquest.io',
    'name': 'Adam Smith',
    'address': '42 Fake Street'
}

cur.execute("INSERT into users VALUES (%(identifier)s, %(mail)s, %(name)s, %(address)s);", row_values)
#=====================================================================================================================


conn.close()


