from .models import Course_record
from rest_framework import serializers

class Course_record_serializer(serializers.ModelSerializer):
     class Meta:
         model = Course_record
         fields = '__all__'