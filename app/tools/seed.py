import sqlite3
from datetime import datetime
import random


def get_ordering() -> list:
    list = []
    while True:
        if len(list) == 10:
            break
        r = random.randint(1, 10)
        if r not in list:
            list.append(r)
    return list

conn = sqlite3.connect('././db.sqlite3')
c = conn.cursor()
c.execute('select id from app_Students')
ids = c.fetchall()
for id in ids:
    ordering = get_ordering()
    course = 1
    for order in ordering:
        sql = f"insert into app_Course_record('course_id','course_order', 'student_id', 'timestamp') values({course},{order}, {id[0]}, '{datetime.now}')"
        print(sql)
        c.execute(sql)
        course+=1
conn.commit()
