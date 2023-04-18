from django.db import models

# Create your models here.
class Credits(models.Model):
    batch = models.CharField(max_length=10, primary_key=True)
    credits1 = models.IntegerField(blank=True, null=True)
    credits2 = models.IntegerField(blank=True, null=True)
    credits3 = models.IntegerField(blank=True, null=True)
    credits4 = models.IntegerField(blank=True, null=True)
    credits5 = models.IntegerField(blank=True, null=True)
    credits6 = models.IntegerField(blank=True, null=True)
    credits7 = models.IntegerField(blank=True, null=True)
    credits8 = models.IntegerField(blank=True, null=True)
    # class Meta:
    #     unique_together = ('specialization', 'batch')
    def __str__(self):
        return self.batch
    

#company model
class Company(models.Model):
    cid = models.CharField(max_length=100, primary_key=True)
    reqCandDet = models.TextField()
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
    password = models.TextField()
    companypic = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.cid
    
#student model
class Student(models.Model):
    roll_no = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.TextField()
    batch=models.ForeignKey(Credits , on_delete=models.CASCADE, related_name='batch_yr',default='2023_CSE')
    cgpa = models.TextField(blank=True, null=True)
    areaofInterest = models.TextField(blank=True, null=True)
    m10 = models.TextField(blank=True, null=True)
    m11 = models.TextField(blank=True, null=True)
    m12 = models.TextField(blank=True, null=True)
    msem1 = models.TextField(blank=True, null=True)
    msem2 = models.TextField(blank=True, null=True)
    msem3 = models.TextField(blank=True, null=True)
    msem4 = models.TextField(blank=True, null=True)
    msem5 = models.TextField(blank=True, null=True)
    msem6 = models.TextField(blank=True, null=True)
    msem7 = models.TextField(blank=True, null=True)
    msem8 = models.TextField(blank=True, null=True)

    # resume = models.FileField(upload_to='resume/', blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    studprofilepic = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
    
#alumni model
class Alumni(models.Model):
    roll_no = models.CharField(max_length=8,primary_key=True)
    name = models.TextField()
    cid=models.ForeignKey(Company , on_delete=models.CASCADE,null=True,blank=True)
    email = models.EmailField()
    password = models.TextField()
    batch=models.ForeignKey(Credits , on_delete=models.CASCADE, related_name='batch_yr_alum',default='2023_CSE')
    cgpa = models.TextField(blank=True, null=True)
    company = models.TextField(null=True,blank=True)
    designation = models.TextField(null=True,blank=True)
    m10 = models.TextField(blank=True, null=True)
    m11 = models.TextField(blank=True, null=True)
    m12 = models.TextField(blank=True, null=True)
    msem1 = models.TextField(blank=True, null=True)
    msem2 = models.TextField(blank=True, null=True)
    msem3 = models.TextField(blank=True, null=True)
    msem4 = models.TextField(blank=True, null=True)
    msem5 = models.TextField(blank=True, null=True)
    msem6 = models.TextField(blank=True, null=True)
    msem7 = models.TextField(blank=True, null=True)
    msem8 = models.TextField(blank=True, null=True)
    ctc=models.TextField(blank=True, null=True)
    area=models.TextField(blank=True,null=True)
    tenure=models.TextField(blank=True, null= True)
    # alumprofilepic = models.ImageField(upload_to='alumprofile_pics/', blank=True, null=True)
    alumprofilepic = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
    
