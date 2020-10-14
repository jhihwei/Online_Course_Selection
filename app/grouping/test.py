from app.models import *
import random
from django.db.models import Min, Max

students_count = Students.objects.all().count()
class_count = Students.objects.values('class_code').distinct().count()
classes_code = Students.objects.distinct('class_code').values('class_code')
classes_code = [row['class_code'] for row in classes_code]
course_count = Course.objects.all().count()
course_code = Course.objects.values('id')
course_code = [row['id'] for row in course_code]
avg_students_every_course = int(students_count/(class_count*course_count))
print(class_count, classes_code, course_code, avg_students_every_course)


def get_volunteer(class_code: int, course_code: int, student_count=avg_students_every_course):
    for i in range(1, student_count+1):
        have_no_allocated = object
        if student_count !=1:
            have_no_allocated = Course_record.objects.filter(
                student__class_code=class_code).filter(allocation=False)
        else:
            have_no_allocated = Course_record.objects.filter(
                course=course_code).filter(allocation=False)

        have_priority = have_no_allocated.filter(course=course_code).values('student')
        have_students = have_priority.order_by('course_order')
        if have_students:
            student = have_students[0]['student']
            # 將該學生標記以分配
            Course_record.objects.filter(
                student=student).update(allocation=True)
            course_id = Course.objects.get(id=course_code)
            students_id = Students.objects.get(id=student)
            course_order = Course_record.objects.filter(student=student).filter(
                course=course_code).values('course_order')
            Group_record.objects.create(
                student=students_id, course=course_id, course_order=course_order, class_code=class_code)
            print(student, class_code, course_code)


# 第一次：平均分配
for course in course_code:
    for class_code in classes_code:
        get_volunteer(class_code, course)
# 第二次：剩餘分配
print(course_code, classes_code)
for class_code in classes_code:
    for course in course_code:
        get_volunteer(class_code=class_code, course_code=course,
                      student_count=1)
