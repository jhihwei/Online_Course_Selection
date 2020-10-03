from app.models import *
import random

students_count = Students.objects.all().count()
class_count = Students.objects.values('class_code').distinct().count()
class_code = Students.objects.distinct('class_code').values('class_code')
class_code = [row['class_code'] for row in class_code]
course_count = Course.objects.all().count()
avg_students_every_course = int(students_count/(class_count*course_count))
print( class_count, class_code)
def get_volunteer():
    for i in range(1, course_count+1):
        print(i)
        have_no_allocated = Course_record.objects.filter(allocation=True)
        have_priority = have_no_allocated.filter(course_order=i)
        have_students = have_priority.values('student').distinct()
        if have_students:
            student = random.sample(list(have_students), 1)
            Course_record.objects.filter(student=student[0]['student']).update(allocation=True)
            print(student[0]['student'])


# get_volunteer()
