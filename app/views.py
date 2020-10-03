import json
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import *
from django.core import serializers
from django.utils.safestring import mark_safe
from django.db import connection

def index(request, present_class=201):
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT class_code FROM app_students order by class_code")
    class_code = [row[0] for row in cursor.fetchall()]
    students = Students.objects.filter(class_code=present_class)
    students = serializers.serialize("json", students)
    course = Course.objects.all()

    return render(request, 'index.html',
                  {'class_code': class_code,
                   'students': mark_safe(students),
                   'course': course})
