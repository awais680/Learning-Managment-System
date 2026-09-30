from django.db import models
from django.contrib.auth.models import User
class course(models.Model):
    class_choices = [('11th','class 11th'),('12th','class 12th')]
    title=models.CharField(max_length=100) #eg math,physics
    class_level=models.CharField(max_length=100) #eg 11 12
    def __str__(self):
        return f'{self.title}-{self.class_level}'

class lesson(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    title=models.CharField(max_length=100) #eg chapter name
    content=models.TextField() # eg chapter detail
    def __str__(self):
        return f"{self.course.title}-{self.title}"
class enrollment(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    enrolled_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.student.username}_{self.course.title}"
    


# Create your models here.
