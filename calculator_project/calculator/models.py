from django.db import models
from django.utils import timezone

# Create your models here.
class CalculationHistory(models.Model):
    num1=models.FloatField()
    num2=models.FloatField()
    operator=models.CharField(max_length=10)
    result=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=timezone.now)


