from django.db import models
from django.contrib.auth.models import User

class Animateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='animateur_photos/', null=True, blank=True)
    classes = models.ManyToManyField('Classe')

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Classe(models.Model):
    nom = models.CharField(max_length=100)
    annee = models.IntegerField()
    categorie = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} ({self.annee} - {self.categorie})"

class Cours(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateField()
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

    def __str__(self):
        return self.nom

class Messe(models.Model):
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

    def __str__(self):
        return f"Messe du {self.date} de {self.heure_debut} à {self.heure_fin}"

class Catechumene(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='catechumene')
    matricule = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    categorie = models.CharField(max_length=20, choices=[('enfant', 'Enfant'), ('jeune', 'Jeune'), ('adulte', 'Adulte')])
    profession_ou_niveau_etude = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now_add=True)
    classe = models.ForeignKey('Classe', on_delete=models.SET_NULL, null=True, blank=True)
    animateur = models.ForeignKey('Animateur', on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField(upload_to='catechumene_photos/', null=True, blank=True)  # Add this line
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Note(models.Model):
    catechumene = models.ForeignKey(Catechumene, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.catechumene.user.username} - {self.cours.nom} - {self.note}"

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='parent_photos/', null=True, blank=True)
    catechumenes = models.ManyToManyField(Catechumene)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Presence(models.Model):
    catechumene = models.ForeignKey(Catechumene, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, null=True, blank=True, on_delete=models.CASCADE)
    messe = models.ForeignKey(Messe, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.catechumene.user.username} - {self.cours or self.messe} - {'Present' if self.present else 'Absent'}"

