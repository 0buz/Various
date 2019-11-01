
# ============= cursor.mogrify ==========================================================
# mogrify is a method for conversion from Python types to Postgres types
from datetime import date
import psycopg2
conn = psycopg2.connect("dbname=test user=pgrole host=localhost password=rpython")
cur = conn.cursor()
game_data = (52499790661213, 'Amazing', 'LittleBigPlanet PS Vita', '/games/littlebigplanet-vita/vita-98907', 'PlayStation Vita', 9.0, 'Platformer', 'y', date(2012, 12, 9))

mogrified_values = cur.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s,%s)", game_data)

print(mogrified_values)  # mogrify returns a bytes object; note the "b" when printing

conn_encoding = conn.encoding   # default UTF8
mogrified_values_decoded = cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", game_data).decode(conn_encoding)   # decode to UTF8 to return str
print(conn_encoding)
print(mogrified_values_decoded)
#==========================================================================================


#================= INSERT multiple rows   =================================================
import csv

with open("ign.csv", "r") as f:
    next(f)
    reader = csv.reader(f)
    rows = [row for row in reader]

mogrified_rows = [cur.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s,%s)", row) for row in rows]
decoded_rows = [mrow.decode(conn.encoding) for mrow in mogrified_rows]

insert_string = ",".join(decoded_rows)

cur.execute("INSERT INTO ign_reviews VALUES " + insert_string + ";")
#==========================================================================================