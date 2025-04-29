from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .models import Child

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')

class AddChildForm(forms.ModelForm):
    GROUP_CHOICES = [
        ('Солнышко', 'Солнышко'),
        ('Дюймовочка', 'Дюймовочка'),
        ('Колокольчик', 'Колокольчик'),
    ]
    
    group = forms.ChoiceField(choices=GROUP_CHOICES, label="Группа")
    
    class Meta:
        model = Child
        fields = ['name', 'age', 'group']
        labels = {
            'name': 'Имя ребенка',
            'age': 'Возраст',
        }
        widgets = {
            'age': forms.NumberInput(attrs={'min': 1, 'max': 7}),
        }