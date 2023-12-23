# Projet de Gestion des Notes

Bienvenue dans le projet de gestion des notes, un système de gestion des matières, étudiants et notations.

### Utilisation ###

Le projet propose des pages pour afficher la liste des matières, des étudiants et des notations. Vous pouvez accéder à ces pages à travers l'interface web.
Il est possible d'ajouter ou de supprimer une donnée pour chacune de ces catégories.

## Installation

Suivez ces étapes pour installer et exécuter le projet localement.

### Prérequis

Assurez-vous d'avoir installé les outils suivants avant de commencer :

- Python 3.x
- Pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Accéder au répertoire du projet**

    cd projet_notes

2. **Créer un environnement virtuel**

    python -m venv venv

3. **Activer l'environnement virtuel**

    **Sur Windows**

        .\venv\Scripts\activate
    
    **Sur Linux/Mac**
        source venv/bin/activate

4. **Installer les dépendances**

    pip install -r requirements.txt

5. **Appliquer les migrations**

    python manage.py migrate

6. **Lancer le serveur de développement**

    python manage.py runserver


Le projet sera accessible à l'adresse : http://localhost:8000/ 







 
