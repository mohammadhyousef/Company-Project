from django import forms
from .models import Project  # Import the Project model

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project  # Specify the model class here
        fields = ['title', 'description', 'image']  # Include all necessary fields