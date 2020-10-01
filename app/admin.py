from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.AdminSite.site_header = '線上選課系統'
# Register your models here.
admin.site.register(Course_record)


@admin.register(Course)
class Course(ImportExportModelAdmin):
    list_display = ('name_code', 'name', 'description')


@admin.register(Students)
class Students(ImportExportModelAdmin):
    list_display = ('class_code', 'number', 'seat_number', 'name', 'gender')
    list_display_links = ('name',)


@admin.register(Group_record)
class Group_record(ImportExportModelAdmin):

    def get_description(self, obj):
        return obj.course.description

    get_description.short_description = '描述'
    list_display = ('course', 'get_description', 'student')
    list_display_links = ('student',)
