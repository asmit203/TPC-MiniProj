from django.db import models

# Create your models here.
class Credits(models.Model):
    specialization = models.CharField(max_length=100)
    batch = models.CharField(max_length=8)
    credits1 = models.IntegerField()
    credits2 = models.IntegerField()
    credits3 = models.IntegerField()
    credits4 = models.IntegerField()
    credits5 = models.IntegerField()
    credits6 = models.IntegerField()
    credits7 = models.IntegerField()
    credits8 = models.IntegerField()
    class Meta:
        unique_together = ('specialization', 'batch')
    def __str__(self):
        return self.batch
    
    
#company model
class Company(models.Model):
    cid = models.CharField(max_length=100)
    reqCandDet = models.TextField()
    minQual = models.TextField()
    marksCriteria = models.TextField()
    salaryPackage = models.TextField()
    mode_of_interview = models.CharField(max_length=50,choices=(
        ('Online_written','Online Written'),
        ('Offline_written','Offline Written'),
        ('Online_interview','Online Interview'),
        ('Offine_interview','Offline Inteview'),
    ))
    time_of_start_iitp = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
#student model
class Student(models.Model):
    roll_no = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    batch = models.CharField(max_length=100, blank=True)
    # branch = models.CharField(max_length=100, blank=True)
    specialization=models.ForeignKey(Credits , on_delete=models.CASCADE)
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
    rollnumber = models.CharField(max_length=8, primary_key=True)
    # cid = models.CharField(max_length=100)
    cid=models.ForeignKey(Company , on_delete=models.CASCADE)
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
    
#credits model
# class Credits(models.Model):
#     specialization = models.CharField(max_length=100)
#     batch = models.CharField(max_length=8)
#     credits = models.IntegerField()
#     class Meta:
#         unique_together = ('specialization', 'batch')
#     def __str__(self):
#         return self.credits