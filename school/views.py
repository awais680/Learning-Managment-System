from django.shortcuts import render
from .models import course,lesson,enrollment
from .serializers import lessonserializer,courseserializer,enrollmentserializer
from rest_framework import viewsets,status,permissions
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import action
from rest_framework.response import Response

class courseviewset(viewsets.ModelViewSet):
    queryset=course.objects.all()
    serializer_class=courseserializer
    @action(detail=False,methods=['get'],url_path='11th')
    def class_11th(self,request):
        courses=course.objects.filter(class_level='11th')
        serializer=self.get_serializer(courses,many=True)
        return Response(serializer.data)
    @action(detail=False,methods=['get'],url_path='12th')
    def class_12th(self):
        courses=course.objects.filter(class_level='12th')
        serializer=self.get_serializer(courses,many=True)
        return Response(serializer.data)

class lessonviewset(viewsets.ModelViewSet):
    queryset=lesson.objects.all()
    serializer_class=lessonserializer
class enrollmentviewset(viewsets.ModelViewSet):
    serializer_class=enrollmentserializer
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        return enrollment.objects.filter(student=self.request.user)
    def perform_create(self,serializer):
        serializer= self.request.user
        serializer.save()
        
    
# Create your views here.
