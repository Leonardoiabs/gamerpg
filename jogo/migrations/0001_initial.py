# Generated by Django 4.1.5 on 2023-02-06 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='NOME DO JOGADOR(A)')),
                ('imagem', models.FileField(upload_to='jogador', verbose_name='IMAGEM')),
            ],
        ),
    ]
