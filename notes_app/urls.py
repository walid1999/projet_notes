from django.urls import path
from notes_app.views import MatiereListView, MatiereCreateView, MatiereUpdateView, MatiereDeleteView
from notes_app.views import EtudiantListView, EtudiantCreateView, EtudiantUpdateView, EtudiantDeleteView
from notes_app.views import NotationListView, NotationCreateView, NotationUpdateView, NotationDeleteView

# urlpatterns est la liste de configurations d'URLs du site.
urlpatterns = [
    path('', MatiereListView.as_view(), name='home'),

    # Configurations pour les pages liées aux matières.
    path('matieres/', MatiereListView.as_view(), name='matiere_list'),
    path('matiere/create/', MatiereCreateView.as_view(), name='matiere_create'),
    path('matiere/<int:pk>/update/', MatiereUpdateView.as_view(), name='matiere_update'),
    path('matiere/<int:pk>/delete/', MatiereDeleteView.as_view(), name='matiere_delete'),

    # Configurations pour les pages liées aux étudiants.
    path('etudiants/', EtudiantListView.as_view(), name='etudiant_list'),
    path('etudiant/create/', EtudiantCreateView.as_view(), name='etudiant_create'),
    path('etudiant/<int:pk>/update/', EtudiantUpdateView.as_view(), name='etudiant_update'),
    path('etudiant/<int:pk>/delete/', EtudiantDeleteView.as_view(), name='etudiant_delete'),

    # Configurations pour les pages liées aux notations.
    path('notations/', NotationListView.as_view(), name='notation_list'),
    path('notation/create/', NotationCreateView.as_view(), name='notation_create'),
    path('notation/<int:pk>/update/', NotationUpdateView.as_view(), name='notation_update'),
    path('notation/<int:pk>/delete/', NotationDeleteView.as_view(), name='notation_delete'),
]
