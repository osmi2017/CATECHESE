from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import ClasseForm, CoursForm, MesseForm, CatechumeneForm, NoteForm, ParentForm, AnimateurForm, ParentForm, PresenceForm
from .models import Classe, Cours, Messe, Catechumene, Presence, Note, Animateur, Parent
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'gestion/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'gestion/dashboard.html')

@login_required
def classes(request):
    classes = Classe.objects.all()
    return render(request, 'gestion/classes.html', {'classes': classes})

@login_required
def cours(request):
    cours_list = Cours.objects.all()
    return render(request, 'gestion/cours.html', {'cours_list': cours_list})

@login_required
def messes(request):
    messes_list = Messe.objects.all()
    return render(request, 'gestion/messes.html', {'messes_list': messes_list})

@login_required
def catechumens(request):
    catechumenes_list = Catechumene.objects.all()
    return render(request, 'gestion/catechumens.html', {'catechumenes_list': catechumenes_list})

@login_required
def parents(request):
    parents_list = Parent.objects.all()
    return render(request, 'gestion/parents.html', {'parents_list': parents_list})

@login_required
def animateur(request):
    animateurs_list = Animateur.objects.all()
    return render(request, 'gestion/animateurs.html', {'animateurs_list': animateurs_list})

@login_required
def presences(request):
    presences = Presence.objects.all()
    return render(request, 'gestion/presences.html', {'presences': presences})

@login_required
def notes(request):
    notes= Note.objects.all()
    return render(request, 'gestion/notes.html', {'notes': notes})

@login_required
def create_messe(request):
    if request.method == 'POST':
        form = ClasseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('messe')
    else:
        form = ClasseForm()
    return render(request, 'gestion/create_messe.html', {'form': form})

@login_required
def update_messe(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return redirect('messe')
    else:
        form = ClasseForm(instance=classe)
    return render(request, 'gestion/update_messe.html', {'form': form})

@login_required
def delete_messe(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        classe.delete()
        return redirect('messe')
    return render(request, 'gestion/delete_messe.html', {'classe': messe})

@login_required
def create_classe(request):
    if request.method == 'POST':
        form = ClasseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes')
    else:
        form = ClasseForm()
    return render(request, 'gestion/create_classe.html', {'form': form})


@login_required
def update_classe(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return redirect('classes')
    else:
        form = ClasseForm(instance=classe)
    return render(request, 'gestion/update_classe.html', {'form': form})

@login_required
def delete_classe(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        classe.delete()
        return redirect('classes')
    return render(request, 'gestion/delete_classe.html', {'classe': classe})

# Repeat the same pattern for Cours, Messe, Catechumene, Note, and Parent
@login_required
def create_cours(request):
    if request.method == 'POST':
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cours')
    else:
        form = CoursForm()
    return render(request, 'gestion/create_cours.html', {'form': form})

@login_required
def update_cours(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    if request.method == 'POST':
        form = CoursForm(request.POST, instance=cours)
        if form.is_valid():
            form.save()
            return redirect('cours')
    else:
        form = CoursForm(instance=cours)
    return render(request, 'gestion/update_cours.html', {'form': form})

@login_required
def delete_cours(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    if request.method == 'POST':
        cours.delete()
        return redirect('cours')
    return render(request, 'gestion/delete_cours.html', {'cours': cours})

@login_required
def create_catechumen(request):
    if request.method == 'POST':
        form = CatechumeneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catechumens')
    else:
        form = CatechumeneForm()
    return render(request, 'gestion/create_catechumene.html', {'form': form})

@login_required
def update_catechumen(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return redirect('catechumen')
    else:
        form = ClasseForm(instance=classe)
    return render(request, 'gestion/update_catechumen.html', {'form': form})

@login_required
def delete_catechumen(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        classe.delete()
        return redirect('catechumen')
    return render(request, 'gestion/delete_catechumen.html', {'classe': catechumen})

@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = NoteForm()
    return render(request, 'gestion/create_note.html', {'form': form})


@login_required
def update_note(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return redirect('note')
    else:
        form = ClasseForm(instance=classe)
    return render(request, 'gestion/update_note.html', {'form': form})

@login_required
def delete_note(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        classe.delete()
        return redirect('note')
    return render(request, 'gestion/delete_note.html', {'classe': note})

@login_required
def create_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST, request.FILES)
        if form.is_valid():
            parent = form.save(commit=False)
            # Create user with default password and link to parent
            user = User.objects.create_user(
                username=f"parent{Parent.objects.count() + 1}",
                password="parent123"
            )
            parent.user = user
            parent.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect('parents')
    else:
        form = ParentForm()
    return render(request, 'gestion/create_parent.html', {'form': form})

@login_required
def update_parent(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return redirect('parent')
    else:
        form = ClasseForm(instance=classe)
    return render(request, 'gestion/update_parent.html', {'form': form})

@login_required
def delete_parent(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        classe.delete()
        return redirect('note')
    return render(request, 'gestion/delete_parent.html', {'classe': parent})

@login_required
def create_animateur(request):
    if request.method == 'POST':
        form = AnimateurForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a unique username
            last_animateur = Animateur.objects.all().order_by('id').last()
            if last_animateur:
                new_id = last_animateur.id + 1
            else:
                new_id = 1
            username = f'animateur{new_id}'
            password = 'animateur123'

            # Create the User
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # Save the Animateur and link the User
            animateur = form.save(commit=False)
            animateur.user = user
            animateur.save()
            form.save_m2m()  # Save the many-to-many data for the form

            return redirect('animateurs')
    else:
        form = AnimateurForm()
    
    return render(request, 'gestion/create_animateur.html', {'form': form})

@login_required
def update_animateur(request, pk):
    animateur = get_object_or_404(Animateur, pk=pk)
    if request.method == 'POST':
        form = AnimateurForm(request.POST, instance=animateur)
        if form.is_valid():
            form.save()
            return redirect('animateurs')
    else:
        form = AnimateurForm(instance=animateur)
    return render(request, 'gestion/update_animateur.html', {'form': form})

@login_required
def delete_animateur(request, pk):
    animateur = get_object_or_404(Animateur, pk=pk)
    if request.method == 'POST':
        animateur.delete()
        return redirect('animateurs')
    return render(request, 'gestion/delete_animateur.html', {'animateur': animateur})

@login_required
def create_presence(request):
    if request.method == 'POST':
        form = PresenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('presences')
    else:
        form = PresenceForm()
    return render(request, 'gestion/create_presence.html', {'form': form})

@login_required
def update_presence(request, pk):
    presence = get_object_or_404(Presence, pk=pk)
    if request.method == 'POST':
        form = PresenceForm(request.POST, instance=presence)
        if form.is_valid():
            form.save()
            return redirect('presences')
    else:
        form = PresenceForm(instance=presence)
    return render(request, 'gestion/update_presence.html', {'form': form})

@login_required
def delete_presence(request, pk):
    presence = get_object_or_404(Presence, pk=pk)
    if request.method == 'POST':
        presence.delete()
        return redirect('presences')
    return render(request, 'gestion/delete_presence.html', {'presence': presence})