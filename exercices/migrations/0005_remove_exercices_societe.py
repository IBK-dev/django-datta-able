# Generated by Django 2.2.10 on 2021-09-25 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercices', '0004_auto_20210923_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercices',
            name='societe',
        ),
    ]
