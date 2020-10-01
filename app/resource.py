from import_export import resources, fileds
from .models import *

class Students(resources.ModelResource):
    class Meta:
        model = Students
        exclude = ('id',)
        skip_unchanged = True
class Course(resources.ModelResource):
    class Meta:
        model = Course
        exclude = ('id', )
        skip_unchanged = True
class Group_record(resources.ModelResource):
    class Meta:
        model = Group_record
        exclude = ('id', )
        skip_unchanged = True

class Course_record(resources.ModelResource):
    class Meta:
        model = Course_record
        exclude = ('id', )
        skip_unchanged = True