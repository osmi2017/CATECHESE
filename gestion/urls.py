from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 path('', views.dashboard, name='dashboard'),
    path('classes/', views.classes, name='classes'),
    path('cours/', views.cours, name='cours'),
    path('messes/', views.messes, name='messes'),
    path('catechumens/', views.catechumens, name='catechumens'),
    path('parents/', views.parents, name='parents'),
    path('animateurs/', views.animateur, name='animateurs'),
    path('notes/', views.notes, name='notes'),
    path('classe/create/', views.create_classe, name='create_classe'),
    path('classe/update/<int:pk>/', views.update_classe, name='update_classe'),
    path('classe/delete/<int:pk>/', views.delete_classe, name='delete_classe'),
    path('cours/create/', views.create_cours, name='create_cours'),
    path('cours/update/<int:pk>/', views.update_cours, name='update_cours'),
    path('cours/delete/<int:pk>/', views.delete_cours, name='delete_cours'),
    path('messe/create/', views.create_messe, name='create_messe'),
    path('messe/update/<int:pk>/', views.update_messe, name='update_messe'),
    path('messe/delete/<int:pk>/', views.delete_messe, name='delete_messe'),
    path('catechumene/create/', views.create_catechumen, name='create_catechumene'),
    path('catechumene/update/<int:pk>/', views.update_catechumen, name='update_catechumene'),
    path('catechumene/delete/<int:pk>/', views.delete_catechumen, name='delete_catechumene'),
    path('note/create/', views.create_note, name='create_note'),
    path('note/update/<int:pk>/', views.update_note, name='update_note'),
    path('note/delete/<int:pk>/', views.delete_note, name='delete_note'),
    path('parent/create/', views.create_parent, name='create_parent'),
    path('parent/update/<int:pk>/', views.update_parent, name='update_parent'),
    path('parent/delete/<int:pk>/', views.delete_parent, name='delete_parent'),
    path('animateur/create/', views.create_animateur, name='create_animateur'),
    path('animateur/update/<int:pk>/', views.update_animateur, name='update_animateur'),
    path('animateur/delete/<int:pk>/', views.delete_animateur, name='delete_animateur'),
    path('presence/', views.presences, name='presence'),
    path('presence/create/', views.create_presence, name='create_presence'),
    path('presence/update/<int:pk>/', views.update_presence, name='update_presence'),
    path('presence/delete/<int:pk>/', views.delete_presence, name='delete_presence'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)