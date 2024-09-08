from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Week(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    week_number = models.IntegerField()

class Lecture(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    video_url = models.URLField()
    pdf_file = models.FileField(upload_to='lectures/')

class Exam(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    question = models.TextField()
    answer_type = models.CharField(max_length=10)  
    # 'MCQ' or 'TF'