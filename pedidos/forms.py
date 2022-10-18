from django import forms
from .models import Pedidos

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['cliente', 'direccion', 'pedido']
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el cliente'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección'}),
            'pedido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese el pedido'}),
        }
        

class UserEditForm(UserChangeForm):
       
       username = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Username'}))
       email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder': 'Email'}))
       first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Nombre'}))
       last_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Apellido'}))
       password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
       #password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
       #password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
       
       class Meta:
        model = User
        fields = [ 'username', 'email', 'first_name', 'last_name', 'password']
        help_texts = {k:"" for k in fields}