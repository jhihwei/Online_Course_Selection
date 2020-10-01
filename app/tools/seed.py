import sqlite3
from datetime import datetime  
conn = sqlite3.connect('././db.sqlite3')
c = conn.cursor()
c.execute('select id from app_Students')
ids = c.fetchall()
for id in ids:
    sql = f"insert into app_Group_record('course_id', 'student_id', 'timestamp') values({1},{id[0]}, '{datetime.now}')"
    print(sql)
    c.execute(sql)
conn.commit()