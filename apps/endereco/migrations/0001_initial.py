# Generated by Django 3.2.12 on 2022-02-25 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=2, verbose_name='Código')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Logradouro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.bairro', verbose_name='Bairro')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('latitude', models.FloatField(default=None, null=True, verbose_name='Latitude')),
                ('longitude', models.FloatField(default=None, null=True, verbose_name='Longitude')),
                ('logradouro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.logradouro', verbose_name='Logradouro')),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.estado', verbose_name='Estado')),
            ],
        ),
        migrations.AddField(
            model_name='bairro',
            name='Cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.cidade', verbose_name='Cidade'),
        ),
    ]
