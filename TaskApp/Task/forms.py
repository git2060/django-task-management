from .models import TaskModel
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model=TaskModel
        fields=["name","description","is_completed","due_date"]