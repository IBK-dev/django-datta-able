# Generated by Django 2.2.10 on 2021-09-25 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encaissements', '0007_auto_20210925_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encaissements',
            name='periode',
        ),
        migrations.RemoveField(
            model_name='encaissements',
            name='societe',
        ),
    ]
