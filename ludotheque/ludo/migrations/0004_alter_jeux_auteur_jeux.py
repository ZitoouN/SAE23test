# Generated by Django 4.0.3 on 2022-06-14 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ludo', '0003_alter_auteurs_photo_aut_alter_jeux_auteur_jeux_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jeux',
            name='auteur_jeux',
            field=models.CharField(max_length=100),
        ),
    ]