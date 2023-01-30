from django import forms
from django.forms import ModelForm
from terreno.models import Terreno


class AddTerrenoForm(ModelForm):

    def clean_nome(self):
        nome = self.cleaned_data['nome'].upper()
        return nome

    class Meta:
        model = Terreno
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_terreno': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }
        fields = [
            'nome',
            'imagem',
            'tipo_terreno',
            'descricao',
        ]
