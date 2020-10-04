from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:present_class>', views.index),
    path('', views.index),
    path('course_record/', views.Course_record_DRF.as_view()),
    path('login', views.login)
]