from django.db import models

# Create your models here.

# #job model
class job(models.Model):
    cid = models.CharField(max_length=100)
    jid = models.CharField(max_length=100, primary_key=True)
    jobTitle = models.CharField(max_length=100)
    jobDesc = models.TextField()

    def __str__(self):
        return self.jobTitle
    

#applied model
class applied(models.Model):
    jid = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=8)
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.roll_no