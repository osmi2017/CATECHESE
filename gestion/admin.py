from django.contrib import admin
from .models import Animateur, Classe, Cours, Messe, Catechumene, Note, Parent, Presence

@admin.register(Animateur)
class AnimateurAdmin(admin.ModelAdmin):
    list_display = ('user', 'classes_list')
    search_fields = ('user__username', 'user__email')
    
    def classes_list(self, obj):
        return ", ".join([cls.nom for cls in obj.classes.all()])
    classes_list.short_description = 'Classes'

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'annee', 'categorie')
    search_fields = ('nom', 'categorie')
    list_filter = ('annee', 'categorie')

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date', 'classe', 'heure_debut', 'heure_fin')
    search_fields = ('nom', 'classe__nom')
    list_filter = ('date', 'classe')

@admin.register(Messe)
class MesseAdmin(admin.ModelAdmin):
    list_display = ('date', 'heure_debut', 'heure_fin')
    search_fields = ('date',)
    list_filter = ('date',)

@admin.register(Catechumene)
class CatechumeneAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'code', 'nom', 'prenom', 'contact', 'categorie', 'profession_ou_niveau_etude', 'date_creation', 'classe', 'animateur', 'photo_preview')
    search_fields = ('nom', 'prenom', 'matricule', 'code', 'contact', 'categorie', 'profession_ou_niveau_etude')
    list_filter = ('categorie', 'classe', 'animateur')
    readonly_fields = ('date_creation',)

    def photo_preview(self, obj):
        if obj.photo:
            return f'<img src="{obj.photo.url}" width="50" height="50" style="border-radius: 50%;">'
        return "No Photo"
    photo_preview.allow_tags = True
    photo_preview.short_description = 'Photo Preview'

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('catechumene', 'cours', 'note')
    search_fields = ('catechumene__user__username', 'cours__nom')
    list_filter = ('cours', 'catechumene')

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('user', 'catechumene_list')
    search_fields = ('user__username', 'user__email')
    
    def catechumene_list(self, obj):
        return ", ".join([c.nom + " " + c.prenom for c in obj.catechumenes.all()])
    catechumene_list.short_description = 'Catéchumènes'

@admin.register(Presence)
class PresenceAdmin(admin.ModelAdmin):
    list_display = ('catechumene', 'cours', 'messe', 'present')
    search_fields = ('catechumene__user__username', 'cours__nom', 'messe__date')
    list_filter = ('present', 'cours', 'messe')

