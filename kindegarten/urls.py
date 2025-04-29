from django.urls import path
from myapp.views import *
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]