from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=30)
    last_name = forms.CharField(label='Last-name:', max_length=30)
    age = forms.IntegerField(label='Age:', )
    email = forms.EmailField(label='Email:')
