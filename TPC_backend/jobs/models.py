from django.db import models
from users.models import Company,Student
# Create your models here.

# #job model
class Job(models.Model):
    cid = models.ForeignKey(Company, on_delete=models.CASCADE)
    jid = models.CharField(max_length=100, primary_key=True)
    jobTitle = models.CharField(max_length=100)
    jobDesc = models.TextField()
    flag_job = models.BooleanField(default=False)
    minQual = models.FloatField(default=7.5)
    # def save(self, *args, **kwargs):
    #     self.minQual = self.cid.minQual # set minQual of job as minQual of company
    #     super().save(*args, **kwargs)
    def __str__(self):
        return self.jid
    

#applied model
class Applied(models.Model):
    jid = models.ForeignKey(Job, on_delete=models.CASCADE)
    # roll_no = models.CharField(max_length=8)
    status = models.CharField(max_length=100)
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='roll_noj')
    def __str__(self):
        return self.roll_no
    