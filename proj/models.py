from django.db import models
import os
# Create your models here.
class TITLE(models.Model):
    title=models.CharField(max_length=50)
    def __str__(self) :
        return self.title

class PROJECT(models.Model):
    code=models.IntegerField()
    nam=models.CharField(max_length=30)
    cost=models.DecimalField(max_digits=15, decimal_places=2)
    duration=models.CharField(max_length=50 ,blank=False)
    modir=models.CharField( max_length=30)
    place=models.TextField()
    pic=models.ImageField(default="", upload_to='proj/images',null=True)
    status=models.BooleanField(default=False)
    desc=models.TextField()
    teedadnafar=models.IntegerField()
    title=models.ForeignKey(TITLE, on_delete=models.CASCADE, default="")
    def __str__(self) :
        return self.nam