from django import forms
from drirfinder.models import Category

class CategoryForm(forms.ModelForm):
	roll_number = forms.CharField(max_length=128, help_text="Roll Number : ")
	year = forms.CharField(widget=forms.Select(choices=Category.YEARS), help_text="Year: ");
	cpi = forms.DecimalField(max_digits=3, decimal_places=2, help_text="CPI : ")
	department = forms.CharField(widget=forms.Select(choices=Category.DEPARTMENTS), help_text="Deparment: ");
	
	class Meta:
		model = Category
		fields = ('roll_number','year','cpi','department')


