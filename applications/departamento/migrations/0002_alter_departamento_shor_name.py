# Generated by Django 4.2.3 on 2023-07-18 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='shor_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre Corto'),
        ),
    ]
