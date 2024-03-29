# Generated by Django 5.0.3 on 2024-03-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('clase1', models.CharField(max_length=20)),
                ('clase2', models.CharField(max_length=20)),
                ('clase3', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Talentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talento1', models.CharField(max_length=20)),
                ('talento2', models.CharField(max_length=20)),
                ('talento3', models.CharField(max_length=20)),
                ('talento4', models.CharField(max_length=20)),
                ('talento5', models.CharField(max_length=20)),
                ('talento6', models.CharField(max_length=20)),
                ('talento7', models.CharField(max_length=20)),
                ('talento8', models.CharField(max_length=20)),
                ('talento9', models.CharField(max_length=20)),
                ('talento10', models.CharField(max_length=20)),
                ('talento11', models.CharField(max_length=20)),
                ('talento12', models.CharField(max_length=20)),
            ],
        ),
    ]
