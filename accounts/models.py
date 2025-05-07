from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Дополнительные поля для родителя
    phone = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"