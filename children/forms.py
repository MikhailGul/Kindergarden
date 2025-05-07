from django import forms
from children.models import Child, KindergartenGroup

class ChildApplicationForm(forms.ModelForm):
    desired_group = forms.ModelChoiceField(
        queryset=KindergartenGroup.objects.all(),
        label="Желаемая группа"
    )
    
    class Meta:
        model = Child
        fields = ['first_name', 'age', 'desired_group']
        labels = {
            'first_name': 'Имя ребенка',
            'age': 'Возраст',
        }

class OpenDayForm(forms.Form):
    parent_name = forms.CharField(
        label="ФИО родителя",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванова Мария Петровна'})
    )
    phone = forms.CharField(
        label="Телефон для связи",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (999) 123-45-67'})
    )