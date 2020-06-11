from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=30)
    age=models.IntegerField()
    sex=models.IntegerField()
    cigsperday = models.IntegerField()
    BPmeds= models.IntegerField(null=True)
    stroke = models.IntegerField()
    hyp = models.IntegerField()
    diabetes = models.IntegerField()
    sisBP = models.IntegerField()
    diaBP = models.IntegerField()
    BMI = models.IntegerField()
    heartrate = models.IntegerField(null=True)
    def __str__(self):
        return self.title
