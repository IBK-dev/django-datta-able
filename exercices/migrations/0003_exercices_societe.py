# Generated by Django 2.2.10 on 2021-09-13 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('societ', '0005_delete_simpleuser'),
        ('exercices', '0002_auto_20210913_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercices',
            name='societe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='societ.Societe'),
        ),
    ]
