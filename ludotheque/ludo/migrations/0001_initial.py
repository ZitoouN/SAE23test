# Generated by Django 4.0.4 on 2022-06-11 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auteurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_aut', models.CharField(max_length=100)),
                ('prenom_aut', models.CharField(max_length=100)),
                ('age_aut', models.IntegerField()),
                ('photo_aut', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cat', models.CharField(max_length=100)),
                ('descriptif_cat', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Joueurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_j', models.CharField(max_length=100)),
                ('prenom_j', models.CharField(max_length=100)),
                ('mail_j', models.EmailField(blank=True, max_length=254, null=True)),
                ('mdp_j', models.CharField(blank=True, max_length=100, null=True)),
                ('type_j', models.CharField(blank=True, choices=[('PARTICULIER', 'Particulier')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jeux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_jeux', models.CharField(max_length=100)),
                ('annee_jeux', models.IntegerField()),
                ('image_jeux', models.ImageField(blank=True, null=True, upload_to='images')),
                ('editeur_jeux', models.CharField(max_length=100)),
                ('auteur_jeux', models.CharField(max_length=100)),
                ('categorie_jeux', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ludo.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_com', models.IntegerField()),
                ('commentaire_jeu', models.TextField(blank=True, null=True)),
                ('date_com', models.DateField(blank=True, null=True)),
                ('jeux_com', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ludo.jeux')),
                ('joueurs_com', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ludo.joueurs')),
            ],
        ),
    ]