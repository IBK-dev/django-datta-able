# Generated by Django 2.2.10 on 2021-09-25 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encaissements', '0005_auto_20210925_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encaissements',
            name='periode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercices.Exercices'),
        ),
    ]