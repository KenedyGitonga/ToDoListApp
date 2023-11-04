from django import forms
from .models import Task

class Taskform(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','description']