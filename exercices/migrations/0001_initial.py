# Generated by Django 2.2.10 on 2021-09-11 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='exercices',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=200)),
                ('Année', models.CharField(max_length=200)),
                ('Prorata', models.CharField(max_length=200)),
            ],
        ),
    ]