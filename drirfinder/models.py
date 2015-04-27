from django.db import models

# Create your models here.
class Category(models.Model):
    roll_number = models.CharField(max_length=128, unique=True, default="0")
    cpi = models.DecimalField( max_digits=2, decimal_places=2, default=0.0)
    department = models.CharField(max_length=128, unique=True, default="null")

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title