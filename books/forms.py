from django import forms 
from .models import BookReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['user_name', 'email', 'text']