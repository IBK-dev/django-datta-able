# Generated by Django 2.2.10 on 2021-09-13 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deductions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numéro_Facture', models.CharField(max_length=200)),
                ('Date_Facture', models.CharField(max_length=200)),
                ('Fournisseur', models.CharField(max_length=200)),
                ('Nature', models.CharField(max_length=200)),
                ('Référence', models.CharField(max_length=200)),
                ('Code_TVA', models.CharField(max_length=200)),
                ('Montant_HT', models.CharField(max_length=200)),
                ('Montant_TVA', models.CharField(max_length=200)),
                ('Montant_TTC', models.CharField(max_length=200)),
                ('Date_paiement', models.CharField(max_length=200)),
                ('Mode_paiement', models.CharField(max_length=200)),
                ('Prorata', models.CharField(max_length=200)),
                ('TVA_déductible', models.CharField(max_length=200)),
                ('Non_resident', models.CharField(max_length=200)),
            ],
        ),
    ]
