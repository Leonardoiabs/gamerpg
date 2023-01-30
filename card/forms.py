from django import forms
from django.forms import ModelForm
from card.models import Card


class AddCardForm(ModelForm):

    def clean_nome(self):
        nome = self.cleaned_data['nome'].upper()
        return nome

    class Meta:
        model = Card
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            # 'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'ataque': forms.TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            'defesa': forms.TextInput(attrs={'type': 'number', 'class': 'form-control'}),
        }
        fields = [
            'nome',
            'imagem',
            'tipo',
            'descricao',
            'ataque',
            'defesa',
        ]

# class AddTerrenoForm(ModelForm):
#
#     def clean_nome(self):
#         nome = self.cleaned_data['nome'].upper()
#         return nome
#
#     class Meta:
#         modal = Terreno
#         widgets = {
#             'nome': forms.TextInput(attrs={'class': 'form-control'}),
#             'tipo': forms.Select(attrs={'class': 'form-control'}),
#             'modificador': forms.IntegerField(attrs={'class': 'form-control'}),
#         }
#         fields = [
#             'nome',
#             'tipo',
#             'modificador'
#         ]