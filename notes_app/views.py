from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Matiere, Etudiant, Notation
from .forms import MatiereForm, EtudiantForm, NotationForm

# Liste des matières
class MatiereListView(ListView):
    model = Matiere  # Utilise le modèle Matiere.
    template_name = 'matiere_list.html'  # Utilise le template 'matiere_list.html'.

# Création d'une matière
class MatiereCreateView(CreateView):
    model = Matiere  # Utilise le modèle Matiere.
    form_class = MatiereForm  # Utilise le formulaire MatiereForm.
    template_name = 'matiere_form.html'  # Utilise le template 'matiere_form.html'.
    success_url = reverse_lazy('matiere_list')  # Redirige vers la liste des matières après une création réussie.

# Mise à jour d'une matière
class MatiereUpdateView(UpdateView):
    model = Matiere  # Utilise le modèle Matiere.
    form_class = MatiereForm  # Utilise le formulaire MatiereForm.
    template_name = 'matiere_form.html'  # Utilise le template 'matiere_form.html'.
    success_url = reverse_lazy('matiere_list')  # Redirige vers la liste des matières après une mise à jour réussie.

# Suppression d'une matière
class MatiereDeleteView(DeleteView):
    model = Matiere  # Utilise le modèle Matiere.
    template_name = 'matiere_confirm_delete.html'  # Utilise le template 'matiere_confirm_delete.html'.
    success_url = reverse_lazy('matiere_list')  # Redirige vers la liste des matières après une suppression réussie.


# Liste des étudiants
class EtudiantListView(ListView):
    model = Etudiant  # Utilise le modèle Etudiant.
    template_name = 'etudiant_list.html'  # Utilise le template 'etudiant_list.html'.

# Création d'un étudiant
class EtudiantCreateView(CreateView):
    model = Etudiant  # Utilise le modèle Etudiant.
    form_class = EtudiantForm  # Utilise le formulaire EtudiantForm.
    template_name = 'etudiant_form.html'  # Utilise le template 'etudiant_form.html'.
    success_url = reverse_lazy('etudiant_list')  # Redirige vers la liste des étudiants après une création réussie.

# Mise à jour d'un étudiant
class EtudiantUpdateView(UpdateView):
    model = Etudiant  # Utilise le modèle Etudiant.
    form_class = EtudiantForm  # Utilise le formulaire EtudiantForm.
    template_name = 'etudiant_form.html'  # Utilise le template 'etudiant_form.html'.
    success_url = reverse_lazy('etudiant_list')  # Redirige vers la liste des étudiants après une mise à jour réussie.

# Suppression d'un étudiant
class EtudiantDeleteView(DeleteView):
    model = Etudiant  # Utilise le modèle Etudiant.
    template_name = 'etudiant_confirm_delete.html'  # Utilise le template 'etudiant_confirm_delete.html'.
    success_url = reverse_lazy('etudiant_list')  # Redirige vers la liste des étudiants après une suppression réussie.


# Liste des notations
class NotationListView(ListView):
    model = Notation  # Utilise le modèle Notation.
    template_name = 'notation_list.html'  # Utilise le template 'notation_list.html'.

# Création d'une notation
class NotationCreateView(CreateView):
    model = Notation  # Utilise le modèle Notation.
    form_class = NotationForm  # Utilise le formulaire NotationForm.
    template_name = 'notation_form.html'  # Utilise le template 'notation_form.html'.
    success_url = reverse_lazy('notation_list')  # Redirige vers la liste des notations après une création réussie.

# Mise à jour d'une notation
class NotationUpdateView(UpdateView):
    model = Notation  # Utilise le modèle Notation.
    form_class = NotationForm  # Utilise le formulaire NotationForm.
    template_name = 'notation_form.html'  # Utilise le template 'notation_form.html'.
    success_url = reverse_lazy('notation_list')  # Redirige vers la liste des notations après une mise à jour réussie.

# Suppression d'une notation
class NotationDeleteView(DeleteView):
    model = Notation  # Utilise le modèle Notation.
    template_name = 'notation_confirm_delete.html'  # Utilise le template 'notation_confirm_delete.html'.
    success_url = reverse_lazy('notation_list')  # Redirige vers la liste des notations après une suppression réussie.

