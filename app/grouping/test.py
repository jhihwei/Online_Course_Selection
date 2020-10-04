from app.models import *
import random

students_count = Students.objects.all().count()
class_count = Students.objects.values('class_code').distinct().count()
classes_code = Students.objects.distinct('class_code').values('class_code')
classes_code = [row['class_code'] for row in classes_code]
course_count = Course.objects.all().count()
course_code = Course.objects.values('id')
course_code = [row['id'] for row in course_code]
avg_students_every_course = int(students_count/(class_count*course_count))
print(class_count, classes_code, course_code)


def get_volunteer(class_code: int, course_code:int):
    for i in range(1, 4):
        print(i)
        have_no_allocated = Course_record.objects.filter(
            student__class_code=class_code).filter(allocation=False)
        have_priority = have_no_allocated.filter(course_order=i)
        have_students = have_priority.values('student').distinct()
        if have_students:
            student = random.sample(list(have_students), 1)[0]['student']
            # 將該學生標記以分配
            Course_record.objects.filter(
                student=student).update(allocation=True)
            course_id = Course.objects.get(id=course_code)
            students_id = Students.objects.get(id=student)
            Group_record.objects.create(student=students_id, course=course_id)
            print(student)

for class_code in classes_code:
    for course in course_code:
        get_volunteer(class_code, course)
