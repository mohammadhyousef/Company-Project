from django import forms
from projects.models import Project  # Assuming you have a Project model in projects/models.py

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image']  # Include all necessary fields

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    recipient = forms.EmailField()       