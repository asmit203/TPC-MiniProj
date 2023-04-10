from django.db import models

# Create your models here.

#student model
class Student(models.Model):
    roll_no = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    cgpa = models.FloatField()
    resume = models.FileField(upload_to='resume/')
    def __str__(self):
        return self.name