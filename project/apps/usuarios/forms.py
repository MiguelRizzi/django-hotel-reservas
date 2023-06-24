from django import forms
from .models import InfoUsuario


class InfoUsuarioForm(forms.ModelForm):
    class Meta:
        model = InfoUsuario
        fields = ['avatar','nacimiento', 'pais', 'provincia', 'ciudad', 'domicilio', 'codigo_postal', 'telefono', 'dni', 'cuit']
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={"class": "form-control"}),
            'provincia': forms.TextInput(attrs={"class": "form-control"}),
            'ciudad': forms.TextInput(attrs={"class": "form-control"}),
            'domicilio': forms.TextInput(attrs={"class": "form-control"}),
            'codigo_postal': forms.TextInput(attrs={"class": "form-control"}),
            'telefono': forms.TextInput(attrs={"class": "form-control"}),
            'dni': forms.TextInput(attrs={"class": "form-control"}),
            'cuit': forms.TextInput(attrs={"class": "form-control"}),
        }
