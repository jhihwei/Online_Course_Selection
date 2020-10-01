import json
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import *
from django.core import serializers
from django.utils.safestring import mark_safe


def index(request, present_class=201):
    class_code = Students.objects.values('class_code').distinct()
    students = Students.objects.filter(class_code=present_class)
    students = serializers.serialize("json", students)
    course = Course.objects.all()

    return render(request, 'index.html',
                  {'class_code': class_code,
                   'students': mark_safe(students),
                   'course': course})
