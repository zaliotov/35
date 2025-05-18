import sqlite3

conn = sqlite3.connect(
     "sports.db"
 )

c = conn.cursor()

c.execute(
     """ 
         CREATE TABLE IF NOT EXISTS STUDENTS (
             ID integer primary key,
             name text,
             lastname text,
             age integer
         )
     """
)

c.executemany(
         'insert into STUDENTS (ID, name, lastname, age) values (?, ?, ?, ?)',
         [(5, 'demetre', 'mefarishvili', 14),
         (4, 'davit', 'metreveli', 13),
         (3, 'misho', 'berishvili', 15),
         (1, 'misho', 'abuashvili', 13),
         (2, 'nikoloz', 'zaliotovi', 13)]
)
c.execute(
     """
         update students
         set name = 'mikheil'
         where id = 3
     """
)

c.execute(
     """
         insert into students (id, name, lastname, age) values (12, 'gio', 'giorgadze', '10')
     """
)

c.execute(
     """
         delete from students where id = 12
     """
)

import sqlite3


c.execute('SELECT * FROM students')
rows = c.fetchall()
conn.close()

for row in rows:
    print(row)