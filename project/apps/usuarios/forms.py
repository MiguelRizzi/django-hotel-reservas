from django import forms
from .models import InfoUsuario


class InfoUsuarioForm(forms.ModelForm):
    class Meta:
        model = InfoUsuario
        fields = ['avatar', 'nacimiento', 'pais', 'provincia', 'ciudad', 'domicilio', 'codigo_postal', 'telefono', 'dni', 'cuit']
        widgets = {
            'avatar': forms.FileInput(),
            'nacimiento': forms.DateInput(),
            'pais': forms.TextInput(),
            'provincia': forms.TextInput(),
            'ciudad': forms.TextInput(),
            'domicilio': forms.TextInput(),
            'codigo_postal': forms.TextInput(),
            'telefono': forms.TextInput(),
            'dni': forms.TextInput(),
            'cuit': forms.TextInput(),
        }

