# Generated by Django 4.2.3 on 2023-07-26 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamento_shor_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name': 'Mi departamento', 'verbose_name_plural': 'Mis departamentos'},
        ),
    ]