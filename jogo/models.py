from django.db import models


class Jogador(models.Model):
    nome = models.CharField(verbose_name='NOME DO JOGADOR(A)', max_length=100)
    imagem = models.FileField(verbose_name='IMAGEM', upload_to='jogador')

