import sqlite3
con = sqlite3.connect("sqlite.db")

c = con.cursor()
c.execute("""CREATE TABLE may(
            First text,
            Last text,
            pay integer)""")

c.execute("INSERT INTO may VALUES('Somit','Pandey',900)")

con.commit()

c.execute("SELECT * FROM may where first='Somit'")

print(c.fetchall())

con.commit()
con.close()