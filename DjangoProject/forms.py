from django import forms
from .models import Contact, Review
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
