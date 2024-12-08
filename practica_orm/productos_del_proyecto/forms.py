from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Importa el modelo de usuario predeterminado de Django
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion']  # Asegúrate de que estos campos existen en tu modelo Producto

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')