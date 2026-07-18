from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):

    DEPARTMENT_CHOICES = [
        ('ENL', 'English Linguistics'),
        ('CIS', 'Computer Systems Engg'),
        ('EL', 'Electronics'),
        ('EE', 'Electrical Engg'),
        ('ME', 'Mechanical Engg'),
    ]

    dept_code = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES, 
        label="Department Code"
    )
    
    class Meta:
        model = Listing
        fields = ['title', 'dept_code', 'condition', 'contact_email']