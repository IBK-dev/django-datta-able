# Generated by Django 2.2.10 on 2021-09-13 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encaissements', '0002_auto_20210913_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encaissements',
            name='Prorata',
        ),
    ]