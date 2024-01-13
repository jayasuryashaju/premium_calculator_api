from django.db import models

class PremiumCalculation(models.Model):
    plan_value = models.CharField(max_length=255)
    sum_assured = models.CharField(max_length = 255)
    age = models.CharField(max_length=255)
    term = models.CharField(max_length=255)
    calculated_premium = models.CharField(max_length= 1000)
