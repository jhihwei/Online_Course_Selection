import psycopg2
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

conn = psycopg2.connect(database="onlineelective", user="postgres", password="1234", host="127.0.0.1", port="5432")
c = conn.cursor()
c.execute('select id from app_Students')
ids = c.fetchall()
for id in ids:
    ordering = get_ordering()
    course = 1
    for order in ordering:
        sql = f"insert into app_Course_record(course_id,course_order, student_id) values({course},{order}, {id[0]})"
        print(sql)
        c.execute(sql)
        course+=1
conn.commit()
