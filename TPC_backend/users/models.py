from django.db import models

# Create your models here.

#student model
class Student(models.Model):
    roll_no = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    batch = models.CharField(max_length=100, blank=True)
    branch = models.CharField(max_length=100, blank=True)
    cgpa = models.FloatField(blank=True)
    areaofInterest = models.TextField(blank=True)
    m10 = models.FloatField(blank=True)
    m11 = models.FloatField(blank=True)
    m12 = models.FloatField(blank=True)
    msem1 = models.FloatField(blank=True)
    msem2 = models.FloatField(blank=True)
    msem3 = models.FloatField(blank=True)
    msem4 = models.FloatField(blank=True)
    msem5 = models.FloatField(blank=True)
    msem6 = models.FloatField(blank=True)
    msem7 = models.FloatField(blank=True)
    msem8 = models.FloatField(blank=True)

    resume = models.FileField(upload_to='resume/', blank=True)
    def __str__(self):
        return self.name
    
#alumni model
class Alumni(models.Model):
    name = models.CharField(max_length=100)
    cid = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    m10 = models.FloatField(blank=True)
    m11 = models.FloatField(blank=True)
    m12 = models.FloatField(blank=True)
    msem1 = models.FloatField(blank=True)
    msem2 = models.FloatField(blank=True)
    msem3 = models.FloatField(blank=True)
    msem4 = models.FloatField(blank=True)
    msem5 = models.FloatField(blank=True)
    msem6 = models.FloatField(blank=True)
    msem7 = models.FloatField(blank=True)
    msem8 = models.FloatField(blank=True)
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
