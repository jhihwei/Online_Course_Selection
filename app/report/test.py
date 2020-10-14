from __future__ import division
import sys
from types import GetSetDescriptorType
import xlsxwriter
import xlrd
import datetime
from app.models import *

students_count = Students.objects.all().count()
class_count = Students.objects.values('class_code').distinct().count()
classes_code = Students.objects.distinct('class_code').values('class_code')
classes_code = [row['class_code'] for row in classes_code]
course_count = Course.objects.all().count()
course_code = Course.objects.values('id')
course_code = [row['id'] for row in course_code]

def get_classes():
    output_file = u"依班級.xlsx"
    wb = xlsxwriter.Workbook(output_file)
    for class_code in classes_code:
        ws = wb.add_worksheet(str(class_code))
        students = Group_record.objects.filter(
            class_code=class_code).all().order_by('student')
        ws.write(0,0,'班級')
        ws.write(0,1,'姓名')
        ws.write(0,2,'課程')
        ws.write(0,3,'志願')
        ws.set_column(0, 0, 30)
        ws.set_column(0, 1, 30)
        ws.set_column(0, 2, 30)
        ws.set_column(0, 3, 30)
        for i, student in enumerate(students):
            ws.write(i+1, 0, str(student.class_code))
            ws.write(i+1, 1, str(student.student))
            ws.write(i+1, 2, str(student.course))
            ws.write(i+1, 3, str(student.course_order))
            print(i, student.course_order, student.class_code,
                student.student, student.course)
    wb.close()

def get_course():
    output_file = u"依課程.xlsx"
    wb = xlsxwriter.Workbook(output_file)
    for course in course_code:
        course_name = Course.objects.get(id=course).name
        ws = wb.add_worksheet(course_name)
        students = Group_record.objects.filter(
            course=course).all().order_by('student')
        ws.write(0,0,'班級')
        ws.write(0,1,'姓名')
        ws.write(0,2,'課程')
        ws.write(0,3,'志願')
        ws.set_column(0, 0, 30)
        ws.set_column(0, 1, 30)
        ws.set_column(0, 2, 30)
        ws.set_column(0, 3, 30)
        for i, student in enumerate(students):
            ws.write(i+1, 0, str(student.class_code))
            ws.write(i+1, 1, str(student.student))
            ws.write(i+1, 2, str(student.course))
            ws.write(i+1, 3, str(student.course_order))
            print(i, student.course_order, student.class_code,
                student.student, student.course)
    wb.close()


# get_classes()
get_course()