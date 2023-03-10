from django import forms
from django.forms import ModelForm
from card.models import Card, Deck, DeckCard


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


class AddDeckForm(ModelForm):

    def clean_nome(self):
        nome = self.cleaned_data['nome'].upper()
        return nome

    class Meta:
        model = Deck
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'jogador': forms.Select(attrs={'class': 'form-control'}),
        }
        fields = [
            'nome',
            'jogador',
        ]


class DeckAddCardForm(ModelForm):

    class Meta:
        model = DeckCard
        widgets = {
            'card': forms.Select(attrs={'class': 'form-control'}),
        }
        fields = [
            'card',
        ]
