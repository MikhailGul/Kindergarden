from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_child, name='add_child'),
    path('gallery/<int:child_id>/', views.child_gallery, name='child_gallery'),
    path('open-day/', views.open_day_registration, name='open_day_registration'),
]