# Generated by Django 4.1.3 on 2023-01-30 10:59

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
                ('Menu', models.CharField(choices=[('', '----'), ('0', 'Menu1'), ('1', 'Menu2'), ('2', 'Menu3')], max_length=10)),
                ('Vieux', models.BooleanField()),
                ('Horaire', models.CharField(choices=[('', '----'), ('0', '7h00'), ('1', '7h30'), ('2', '8h00'), ('3', '8h30'), ('4', '9h00'), ('5', '9h30'), ('6', '10h00'), ('7', '10h30'), ('8', '11h00'), ('9', '11h30'), ('10', '12h00'), ('11', '12h30'), ('12', '13h00'), ('13', '13h30'), ('14', '14h00'), ('15', '14h30'), ('16', '15h00'), ('17', '15h30'), ('18', '16h00'), ('19', '16h30'), ('20', '17h00')], max_length=10)),
                ('Couvert', models.BooleanField()),
                ('Message', models.TextField(blank=True, max_length=200)),
            ],
        ),
    ]
