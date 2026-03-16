
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    
    
    path('cours/', views.liste_cours, name='liste_cours'),
    path('cours/ajouter/', views.ajouter_cours, name='ajouter_cours'),
    path('cours/<int:id>/modifier/', views.modifier_cours, name='modifier_cours'),
    path('cours/<int:id>/supprimer/', views.supprimer_cours, name='supprimer_cours'),
    
   
    path('enseignants/', views.liste_enseignant, name='liste_enseignant'),
    path('enseignants/ajouter/', views.ajouter_enseignant, name='ajouter_enseignant'),
    path('enseignants/<int:id>/modifier/', views.modifier_enseignant, name='modifier_enseignant'),
    path('enseignants/<int:id>/supprimer/', views.supprimer_enseignant, name='supprimer_enseignant'),

    path('connexion/', views.connexion_utilisateur, name='connexion'), 
    path('deconnexion/', views.deconnexion_utilisateur, name='deconnexion'), 

]