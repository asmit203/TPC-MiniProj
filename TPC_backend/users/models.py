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
    
#alumni model
class Alumni(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
#company model
class Company(models.Model):
    cid = models.CharField(max_length=100)
    reqCandDet = models.TextField()
    minQual = models.TextField()
    marksCriteria = models.TextField()
    salaryPackage = models.TextField()
    mode_of_interview = models.TextField()
    time_of_start_iitp = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name
