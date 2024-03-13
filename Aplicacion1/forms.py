from django import forms

class JugadoresForm(forms.Form):
    nombre = forms.CharField(max_length=20, required=True)
    apellido = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)

class PersonajesForm(forms.Form):
    nombre = forms.CharField(max_length=20, required=True)

class TalentosForm(forms.Form):
    nombre = forms.CharField(max_length=20, required=True)