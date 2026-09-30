from django.urls import path,include
from .views import courseviewset,lessonviewset,enrollmentviewset
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'courses',courseviewset,basename='course')
router.register(r'lessons',lessonviewset,basename='lesson')
router.register(r'enrollments',enrollmentviewset,basename='enrollment')

urlpatterns = [
    path('school/',include(router.urls)),
    path('api_auth/',include('rest_framework.urls')),
]
