from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['foto', 'title', 'author', 'description', 'is_read', 'date_read', 'rating']
        widgets = {
            'date_read': forms.DateInput(attrs={'type': 'date'}),
        }