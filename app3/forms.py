from pyexpat import model
from socket import fromshare
from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

        class Meta:
            model= Contacto
            fields =["nombre", "correo", "tipo_consulta", "mensaje","avisos"]

class ProductoForm(forms.ModelForm):
        class Meta:
            model=Producto
            fields= '__all__'
            
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'first_name','last_name', "email", "password1","password2"]
        