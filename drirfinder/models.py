from django.db import models

# Create your models here.
class Category(models.Model):
    roll_number = models.CharField(max_length=128, unique=True, default="0")
    cpi = models.DecimalField( max_digits=3, decimal_places=2, default=0.0)
    department = models.CharField(max_length=128, default="null")

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.roll_number

