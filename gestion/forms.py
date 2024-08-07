from django import forms
from django.contrib.auth.models import User
from .models import Classe, Cours, Messe, Catechumene, Note, Parent, Animateur, Presence
from django.db import transaction

class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = ['nom', 'annee', 'categorie']

class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['nom', 'date', 'classe', 'heure_debut', 'heure_fin']

class MesseForm(forms.ModelForm):
    class Meta:
        model = Messe
        fields = ['date', 'heure_debut', 'heure_fin']

class CatechumeneForm(forms.ModelForm):
    class Meta:
        model = Catechumene
        fields = [
            'matricule', 
            'code', 
            'nom', 
            'prenom', 
            'contact', 
            'categorie', 
            'profession_ou_niveau_etude', 
            'classe', 
            'animateur',
            'photo'
        ]

    def save(self, commit=True):
        with transaction.atomic():
            user_count = User.objects.filter(username__startswith='catechumene').count()
            username = f'catechumene{user_count + 1}'
            user = User.objects.create_user(
                username=username,
                password='cate123'
            )
            catechumene = super().save(commit=False)
            catechumene.user = user

            if commit:
                catechumene.save()
                
            return catechumene

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['catechumene', 'cours', 'note']

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['user', 'catechumenes']

class AnimateurForm(forms.ModelForm):
    class Meta:
        model = Animateur
        fields = ['nom', 'prenom', 'contact', 'photo', 'classes']

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['nom', 'prenom', 'contact', 'photo', 'catechumenes']

class PresenceForm(forms.ModelForm):
    class Meta:
        model = Presence
        fields = ['catechumene', 'cours', 'messe', 'date', 'present']
     
