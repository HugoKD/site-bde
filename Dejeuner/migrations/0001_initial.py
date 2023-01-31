# Generated by Django 4.1.3 on 2023-01-31 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prenom', models.CharField(max_length=20)),
                ('Nom', models.CharField(max_length=20)),
                ('Num', models.CharField(max_length=10)),
                ('Adresse', models.CharField(max_length=30)),
                ('Vieux', models.BooleanField()),
                ('Couvert', models.BooleanField()),
                ('Horaire', models.CharField(max_length=10)),
                ('Menu', models.CharField(max_length=10)),
                ('Message', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceDispo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Horaire', models.CharField(max_length=5)),
                ('Count', models.IntegerField(verbose_name=20)),
            ],
        ),
    ]
