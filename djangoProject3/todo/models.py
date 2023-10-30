from django.db import models
from django.utils import timezone


class Utilisateur(models.Model):
    email = models.EmailField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField('date de naissance')


class Rating(models.Model):
    id_commentaire = models.IntegerField(primary_key=True)
    commentaire = models.CharField(max_length=255)
    note = models.BooleanField()
    films = models.ManyToManyField(Film)


class Film(models.Model):
    id_film = models.IntegerField(primary_key=True)
    desciption = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    affiche = models.ImageField()
    titre = models.CharField(max_length=100)
    date = models.DateField('date de sortie')
    acteur = models.CharField(max_length=50)
    pass


class Seance(models.Model):
    id_seance = models.IntegerField(primary_key=True)
    horaire = models.DateTimeField('date et heure de la séance')
    places_reservees = models.IntegerField()


# blank = true c'est pour dire que le champs n'est pas obligatoire#
# je l'ai mis pour le nombre de placr car il peut ne pas en commander
# ou alors il vaut mieux le laisser obligatoire et mettre un 0 qd il commande rien
class Type_salle(models.Model):
    num_salle = models.IntegerField(primary_key=True)
    lieu = models.CharField(max_length=30)
    nmbre_place = models.IntegerField(blank=True)
    prix = models.FloatField()

