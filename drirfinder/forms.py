from django import forms
from drirfinder.models import Category

class CategoryForm(forms.ModelForm):
    roll_number = forms.CharField(max_length=128, help_text="Roll Number : ")
    cpi = forms.DecimalField(max_digits=3, decimal_places=2, help_text="CPI : ")
    department = forms.CharField(max_length=128 , help_text="Department : ");

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('roll_number','cpi','department')


