from django.contrib import admin
from children.models import KindergartenGroup, Child, ChildPhoto
from django.core.mail import send_mail
from django.conf import settings
from .models import OpenDayRegistration

@admin.register(OpenDayRegistration)
class OpenDayRegistrationAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'phone', 'registration_date')
    list_filter = ('registration_date',)
    search_fields = ('parent_name', 'phone')

class ChildPhotoInline(admin.TabularInline):
    model = ChildPhoto
    extra = 1

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'age', 'parent', 'group', 'status')
    list_filter = ('status', 'group')
    search_fields = ('first_name', 'parent__first_name', 'parent__last_name')
    inlines = [ChildPhotoInline]
    actions = ['approve_children', 'reject_children']
    
    def save_model(self, request, obj, form, change):
        if obj.status == 'approved' and not change:  # Если ребенка только что одобрили
            super().save_model(request, obj, form, change)
            obj.create_default_gallery()
        else:
            super().save_model(request, obj, form, change)

    def approve_children(self, request, queryset):
        queryset.update(status='approved')
        for child in queryset:
            send_mail(
                'Заявка одобрена',
                f'Ваша заявка на ребенка {child.first_name} была одобрена!',
                settings.DEFAULT_FROM_EMAIL,
                [child.parent.email],
                fail_silently=False,
            )
        self.message_user(request, "Выбранные заявки одобрены")
    
    def reject_children(self, request, queryset):
        queryset.update(status='rejected')
        for child in queryset:
            send_mail(
                'Заявка отклонена',
                f'Ваша заявка на ребенка {child.first_name} была отклонена.',
                settings.DEFAULT_FROM_EMAIL,
                [child.parent.email],
                fail_silently=False,
            )
        self.message_user(request, "Выбранные заявки отклонены")
    
    approve_children.short_description = "Одобрить выбранные заявки"
    reject_children.short_description = "Отклонить выбранные заявки"

@admin.register(KindergartenGroup)
class KindergartenGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_range')
    search_fields = ('name',)

admin.site.register(ChildPhoto)