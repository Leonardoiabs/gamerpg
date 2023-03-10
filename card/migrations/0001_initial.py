# Generated by Django 4.1.5 on 2023-01-27 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('imagem', models.FileField(upload_to='cards')),
                ('descricao', models.TextField(max_length=1000)),
                ('ataque', models.IntegerField()),
                ('defesa', models.IntegerField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='card.tipo')),
            ],
        ),
    ]
