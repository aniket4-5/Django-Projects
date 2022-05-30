from dataclasses import field, fields
import email
from django import forms
from .models import Emp


class Empreg(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'})
        }
