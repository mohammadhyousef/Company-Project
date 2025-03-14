from django.db import models 
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # إضافة related_name لتجنب التعارض مع الحقول الافتراضية في auth.User
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_groups', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_permissions', 
        blank=True
    )