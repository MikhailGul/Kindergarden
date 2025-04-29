from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Child

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительно', {'fields': ('phone',)}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Child)