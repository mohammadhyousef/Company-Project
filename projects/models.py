from django.db import models 
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth import get_user_model 

User = get_user_model()

class Project(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    description = models.TextField(_('Description'))
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title