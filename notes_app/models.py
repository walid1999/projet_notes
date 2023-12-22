from django.db import models

class Matiere(models.Model):
    nom = models.CharField(max_length=255)  # Champ pour le nom de la matière.
    code = models.CharField(max_length=20)  # Champ pour le code de la matière.

    def __str__(self):
        return self.nom  # Affiche le nom de la matière lorsqu'il est converti en chaîne.

    class Meta:
        app_label = 'notes_app'  # Spécifie l'étiquette de l'application pour éviter des conflits lors des migrations.

class Etudiant(models.Model):
    nom = models.CharField(max_length=255)  # Champ pour le nom de l'étudiant.
    prenom = models.CharField(max_length=255)  # Champ pour le prénom de l'étudiant.
    numero_etudiant = models.CharField(max_length=20, unique=True)  # Champ pour le numéro d'étudiant unique.

    def __str__(self):
        return f"{self.nom} {self.prenom}"  # Affiche le nom complet de l'étudiant lorsqu'il est converti en chaîne.

    class Meta:
        app_label = 'notes_app'  # Spécifie l'étiquette de l'application pour éviter des conflits lors des migrations.


class Notation(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)  # Relation avec le modèle Matiere.
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)  # Relation avec le modèle Etudiant.
    note = models.DecimalField(max_digits=5, decimal_places=2)  # Champ pour la note de l'étudiant.
    date_notation = models.DateField()  # Champ pour la date de notation.

    def __str__(self):
        return f"{self.etudiant} - {self.matiere} - {self.note}"  # Affiche les détails de la notation lorsqu'il est converti en chaîne.

    class Meta:
        app_label = 'notes_app'  # Spécifie l'étiquette de l'application pour éviter des conflits lors des migrations.
