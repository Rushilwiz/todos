from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...', 'id':'input-box'}))
    
    class Meta:
        model = Task
        fields = ('title',)