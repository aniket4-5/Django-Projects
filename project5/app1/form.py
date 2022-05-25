from dataclasses import field
from importlib.metadata import files
from django import forms
from app1.models import Post

class addPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
    