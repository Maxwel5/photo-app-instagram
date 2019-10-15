from django import forms

class InstagramForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=20)
    email = forms.EmailField(label='Email')