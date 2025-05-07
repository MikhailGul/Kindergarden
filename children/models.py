from django.db import models
from accounts.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from django.conf import settings

class OpenDayRegistration(models.Model):
    parent_name = models.CharField(max_length=100, verbose_name="ФИО родителя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.parent_name} ({self.phone})"

class KindergartenGroup(models.Model):
    name = models.CharField(max_length=100)
    age_range = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Child(models.Model):
    STATUS_CHOICES = [
        ('pending', 'На рассмотрении'),
        ('approved', 'Одобрено'),
        ('rejected', 'Отклонено'),
    ]
    
    parent = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    group = models.ForeignKey(KindergartenGroup, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} ({self.age} лет)"
    
    def create_default_gallery(self):
        """Создает стандартную галерею для ребенка"""
        default_images = [
            'default/gallery1.jfif',
            'default/gallery2.jfif',
            'default/gallery3.jfif'
        ]

        for img in default_images:
            default_image_path = os.path.join(settings.MEDIA_ROOT, img)
            if os.path.exists(default_image_path):
                ChildPhoto.objects.create(
                    child=self,
                    image=img
                )

    
    def save(self, *args, **kwargs):
        created = not self.pk  # Проверяем, создается ли новый объект
        super().save(*args, **kwargs)
        
        if created and self.status == 'approved':
            self.create_default_gallery()

    def __str__(self):
        return f"{self.first_name} ({self.age} лет)"

class ChildPhoto(models.Model):
    child = models.ForeignKey(Child, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='children_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Фото {self.child.first_name}"
    
@receiver(post_save, sender=Child)
def create_child_gallery(sender, instance, created, **kwargs):
    """Создает галерею при создании ребенка"""
    if created and instance.status == 'approved':
        instance.create_default_gallery()