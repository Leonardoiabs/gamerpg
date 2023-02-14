from django.db import models


class Jogador(models.Model):
    nome = models.CharField(verbose_name='NOME DO JOGADOR(A)', max_length=100)
    imagem = models.FileField(verbose_name='IMAGEM', upload_to='jogador')

    def __str__(self):
        return self.nome

class Partida(models.Model):
    deck = models.ForeignKey('card.Deck', on_delete=models.DO_NOTHING, verbose_name='DECK', related_name='partida_deck')