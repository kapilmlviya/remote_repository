from django.db import models
class feedbackData(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateTimeField(max_length=100)
    feedback=models.CharField(max_length=100)

# Create your models here.
