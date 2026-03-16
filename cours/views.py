from django.shortcuts import render, redirect, get_object_or_404
from .forms import CoursForm, EnseignantForm
from .models import Cours, Enseignant
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required

# Create your views here.

#def accueil(request):
    #context = {
       # 'total_cours': Cours.objects.count(),
       # 'total_enseignants': Enseignant.objects.count(),
    #}
   # return render(request, 'cours/accueil.html', context)

def connexion_utilisateur(request):
    message = "" 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('liste_cours') 
        else:
            message = "Nom d'utilisateur ou mot de passe incorrect."
    return render(request, 'cours/connexion.html', {'message': message})


def deconnexion_utilisateur(request): 
    logout(request) 
    return redirect('connexion') 

def accueil(request):
    return render(request, 'cours/accueil.html')    

@login_required
def liste_cours(request):
    cours = Cours.objects.all()
    return render(request, 'cours/liste_cours.html', {'cours': cours})

@login_required
def ajouter_cours(request):
    form = CoursForm()
    if request.method == 'POST':
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_cours')
    return render(request, 'cours/ajouter_cours.html', {'form': form})

@login_required
def modifier_cours(request, id):
    cours = get_object_or_404(Cours, id=id)
    form = CoursForm(instance=cours)
    
    if request.method == 'POST':
        form = CoursForm(request.POST, instance=cours)
        if form.is_valid():
            form.save()
            return redirect('liste_cours')
    
    return render(request, 'cours/modifier_cours.html', {'form': form, 'cours': cours})

@login_required
def supprimer_cours(request, id):
    cours = get_object_or_404(Cours, id=id)
    
    if request.method == 'POST':
        cours.delete()
        return redirect('liste_cours')
    
    return render(request, 'cours/supprimer_cours.html', {'cours': cours})

@login_required
def liste_enseignant(request):
    enseignant = Enseignant.objects.all()
    return render(request, 'cours/liste_enseignant.html', {'enseignant': enseignant})

@login_required
def ajouter_enseignant(request):
    form = EnseignantForm()
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_enseignant')
    return render(request, 'cours/ajouter_enseignant.html', {'form': form})



@login_required
def modifier_enseignant(request, id):
    enseignant = get_object_or_404(Enseignant, id=id)
    form = EnseignantForm(instance=enseignant)
    
    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('liste_enseignant')
    
    return render(request, 'cours/modifier_enseignant.html', {'form': form, 'enseignant': enseignant})

@login_required
def supprimer_enseignant(request, id):
    enseignant = get_object_or_404(Enseignant, id=id)
    
    if request.method == 'POST':
        enseignant.delete()
        return redirect('liste_enseignant')
    
    return render(request, 'cours/supprimer_enseignant.html', {'enseignant': enseignant})