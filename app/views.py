from app.serializers import Course_record_serializer
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from django.db import transaction
from django.contrib.auth import authenticate, login as dj_login
import json
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import *
from django.core import serializers
from django.utils.safestring import mark_safe
from django.db import connection
from django.contrib import auth


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if request.POST:
            user = authenticate(
                username=request.POST.get('username'), 
                password=request.POST.get('password'))
            if user is not None:
                dj_login(request, user)
                return HttpResponseRedirect("/")
            else:
                return render(request, 'login.html')
        return render(request, 'login.html')

def index(request, present_class=201):
    # if request.user.is_authenticated:
    if True:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT DISTINCT class_code FROM app_students order by class_code")
        class_code = [row[0] for row in cursor.fetchall()]
        students = Students.objects.filter(class_code=present_class)
        students = serializers.serialize("json", students)
        course = Course.objects.all()

        return render(request, 'index.html',
                    {'class_code': class_code,
                    'students': mark_safe(students),
                    'course': course})
    else:
        return HttpResponseRedirect("/login")


class Course_record_DRF(GenericAPIView):
    queryset = Course_record.objects.all()
    serializer_class = Course_record_serializer

    def get(self, request, *args, **krgs):
        record = self.get_queryset()
        serializer = self.serializer_class(record, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)

    def post(self, request, *args, **krgs):
        data = request.data
        student_id = data.get('student')
        order = data.getlist('order[]')
        try:
            if not Course_record.objects.filter(student=student_id):
                for i, v in enumerate(order):
                    course = Course.objects.get(id=v)
                    student = Students.objects.get(id=student_id)
                    Course_record.objects.create(student=student,
                                                 course=course, course_order=i+1)
                return HttpResponse("ok")
            else:
                return HttpResponse("assigned")
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data)
