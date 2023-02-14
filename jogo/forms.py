from django import forms
from django.forms import ModelForm
from jogo.models import Jogador, Partida


class AddJogadorForm(ModelForm):

    def clean_nome(self):
        nome = self.cleaned_data['nome'].upper()
        return nome

    class Meta:
        model = Jogador
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }
        fields = [
            'nome',
            'imagem',
        ]


class AddDeckPartida(ModelForm):

    class Meta:
        model = Partida

        fields = [
            'deck',
        ]
