from django.db import models

# Create your models here.
class Category(models.Model):
	DEPARTMENTS = (
		('CSE' , 'Computer Science and Engineering'),
		('EE' , 'Electrical Engineering'),
		('ME' , 'Mechanical Engineering'),
		('MEMS' , 'Metallurgy and Material Science'),
		('CE' , 'Civil Engineering'),
		('CL' , 'Chemical Engineering'),
		('EP' , 'Engineering Physics'),
		('ESE' , 'Energy Science and Engineering'),
		('AE' , 'Aerospace Engineering'),
		('CH' , 'Chemistry'),
		)
	YEARS = (
		('1' , 'Freshie'),
		('2' , 'Sophie'),
		('3' , 'Thirdie'),
		('4' , 'Fourthie'),
		)
	roll_number = models.CharField(max_length=128, unique=True, default="0")
	cpi = models.DecimalField( max_digits=3, decimal_places=2, default=0.0)
	department = models.CharField(max_length=4, choices=DEPARTMENTS)
	year = models.CharField(max_length=1, choices=YEARS)
	def __unicode__(self):
		return self.roll_number

