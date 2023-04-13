from django.db import models
from users.models import Company,Student
# Create your models here.

# #job model
class job(models.Model):
    cid = models.ForeignKey(Company, on_delete=models.CASCADE)
    jid = models.CharField(max_length=100, primary_key=True)
    jobTitle = models.CharField(max_length=100)
    jobDesc = models.TextField()
    flag_job = models.BooleanField()


    def __str__(self):
        return self.jobTitle
    

#applied model
class applied(models.Model):
    jid = models.ForeignKey(job, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=8)
    status = models.CharField(max_length=100)
    sid = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return self.roll_no
    