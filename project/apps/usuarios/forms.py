from django import forms
from .models import InfoUsuario


class InfoUsuarioForm(forms.ModelForm):
    class Meta:
        model = InfoUsuario
        fields = ['avatar', 'nacimiento', 'pais', 'provincia', 'ciudad', 'domicilio', 'codigo_postal', 'telefono', 'dni', 'cuit']


