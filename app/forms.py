from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Creamos un template del formulario
class SeguroForm (forms.ModelForm):

    class Meta: 
        model = Seguro
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','password1','password2']

class ReporteCursoForm(forms.ModelForm):
    class Meta:
        model = ReporteCurso
        fields = '__all__'