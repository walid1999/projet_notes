from django import forms
from .models import Matiere, Etudiant, Notation

class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere # Utilise le modèle Matière.
        fields = ['nom', 'code'] #Les champs à renseigner du formulaire.

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant # Utilise le modèle Etudiant.
        fields = ['nom', 'prenom', 'numero_etudiant'] #Les champs à renseigner du formulaire.

class NotationForm(forms.ModelForm):
    class Meta:
        model = Notation # Utilise le modèle Notation.
        fields = ['matiere', 'etudiant', 'note', 'date_notation'] #Les champs à renseigner du formulaire.
