# Generated by Django 2.2.10 on 2021-09-13 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encaissements', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exercices',
            new_name='Encaissements',
        ),
    ]