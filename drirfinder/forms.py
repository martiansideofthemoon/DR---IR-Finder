from django import forms
from drirfinder.models import Category

class CategoryForm(forms.ModelForm):
    roll_number = forms.CharField(max_length=128, help_text="Please enter your roll number.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)

