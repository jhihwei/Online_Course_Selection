from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.AdminSite.site_header = '線上選課系統'
# Register your models here.


@admin.register(Course)
class Course_admin(ImportExportModelAdmin):
    list_display = ('name_code', 'name', 'description')


@admin.register(Students)
class Students_admin(ImportExportModelAdmin):
    list_display = ('class_code', 'number', 'seat_number', 'name', 'gender')
    list_display_links = ('name',)


@admin.register(Group_record)
class Group_record_admin(ImportExportModelAdmin):

    def get_description(self, obj):
        return obj.course.description
    get_description.short_description = '描述'

    def get_class_code(self, obj):
        return obj.student.class_code
    get_class_code.short_description = '班級'

    list_display = ('course', 'get_description', 'get_class_code', 'student')
    list_display_links = ('student',)
    readonly_fields=('student', 'timestamp')

@admin.register(Course_record)
class Course_record_admin(ImportExportModelAdmin):
    def get_description(self, obj):
        return obj.course.description
    get_description.short_description = '描述'

    def get_class_code(self, obj):
        return obj.student.class_code
    get_class_code.short_description = '班級'

    def get_seat_number(self, obj):
        return obj.student.seat_number
    get_seat_number.short_description = '座號'

    list_display = ('course', 'get_description', 'get_class_code', 'get_seat_number', 'student', 'course_order', 'allocation', 'timestamp')
    list_display_links = ('student',)
    search_fields = ['student__class_code']