from rest_framework import serializers
from .models import course,lesson,enrollment

class lessonserializer(serializers.ModelSerializer):
    class Meta:
        model=lesson
        fields=['id','course','title','content']
class courseserializer(serializers.ModelSerializer):
    lesson=lessonserializer(many=True,read_only=True)
    class Meta:
        model=course
        fields=['id','title','class_level','lesson']
class enrollmentserializer(serializers.ModelSerializer):
    course=courseserializer(many=True,read_only=True)
    class Meta:
        model=enrollment
        fields=['id','student','enrolled_at','course']
