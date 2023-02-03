from django.db import models


class TipoDoTerreno(models.Model):
    nome = models.CharField(max_length=100)
    ataque_positivo = models.IntegerField(verbose_name='AUMENTO DE ATAQUE')
    defesa_positiva = models.IntegerField(verbose_name='AUMENTO DE DEFESA')
    ataque_negativo = models.IntegerField(verbose_name='REDUÇÃO DE ATAQUE')
    defesa_negativa = models.IntegerField(verbose_name='REDUÇÃO DE DEFESA')


class Terreno(models.Model):
    nome = models.CharField(verbose_name='NOME DO TERRENO', max_length=100)
    imagem = models.FileField(verbose_name='IMAGEM', upload_to='terreno')
    tipo_terreno = models.ForeignKey(TipoDoTerreno, on_delete=models.DO_NOTHING,verbose_name='TIPO DE TERRENO')
    descricao = models.TextField(verbose_name='DESCRICAO', max_length=1000)

    def __str__(self):
        return self.nome
