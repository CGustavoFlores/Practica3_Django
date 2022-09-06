from pyexpat import model
from socket import fromshare
from django import forms
from .models import Contacto, Producto

class ContactoForm(forms.ModelForm):

        class Meta:
            model= Contacto
            fields =["nombre", "correo", "tipo_consulta", "mensaje","avisos"]

class ProductoForm(forms.ModelForm):
        class Meta:
            model=Producto
            fields= '__all__'
            
