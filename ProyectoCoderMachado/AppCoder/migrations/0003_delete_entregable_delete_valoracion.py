# Generated by Django 5.0 on 2023-12-24 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_valoracion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Valoracion',
        ),
    ]
