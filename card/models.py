from django.db import models


class Tipo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Card(models.Model):
    nome = models.CharField(verbose_name='NOME DA CARTA', max_length=100)
    imagem = models.FileField(verbose_name='IMAGEM', upload_to='cards')
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING, verbose_name='TIPO')
    descricao = models.TextField(verbose_name='DESCRICAO', max_length=1000)
    ataque = models.IntegerField(verbose_name='PODER DE ATAQUE')
    defesa = models.IntegerField(verbose_name='PODER DE DEFESA')


# class TipoDeTerreno(models.Model):
#     nome = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.nome
#
#
# class Terreno(models.Model):
#     nome = models.CharField(verbose_name='NOME DO TERRENO', max_length=100)
#     tipo = models.ManyToManyField(TipoDeTerreno, verbose_name='TIPO DE TERRENO')
#     modificador = models.IntegerField(verbose_name='MODIFICADOR DO TERRENO')
