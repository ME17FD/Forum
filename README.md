# Forum Django

Un projet de forum développé avec le framework Django. Ce site permet aux utilisateurs de s'inscrire, de créer des discussions, de répondre aux publications, et de participer à des discussions communautaires.

## Fonctionnalités

- **Gestion des utilisateurs :** Inscription, connexion, déconnexion, gestion de profil.
- **Création de forums et de sujets :** Les utilisateurs peuvent créer des sujets et publier des messages.
- **Commentaires :** Réponses aux messages dans les sujets.
- **Catégorisation :** Organisation des discussions en catégories.
- **Modération :** Suppression/édition de messages par les administrateurs.
- **Notifications :** (Optionnel) Alertes pour les réponses ou les mentions.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- Python 3.12
- Django 5.1
- SQLite3
- Pillow
- pip (pour gérer les dépendances Python)

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/votre-utilisateur/forum-django.git
   cd forum-django
   ```
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3.Configurez la base de données :
   ```bash
    python manage.py migrate
   ```
4.Lancez le serveur de développement :
   ```bash
    python manage.py runserver
   ```
5.Accédez à l'application dans votre navigateur à l'adresse http://127.0.0.1:8000/.