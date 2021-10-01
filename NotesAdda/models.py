from django.db import models

# Create your models here.
class uploadFiles(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    uni_coll = models.CharField(max_length=100)
    branchName = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    semName = models.PositiveSmallIntegerField()
    date= models.DateField(auto_now=True)
    myFile =models.FileField(upload_to='pdfs/')




#models for uploading pdfs

