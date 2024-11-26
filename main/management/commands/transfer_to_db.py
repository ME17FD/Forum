from django.core.management.base import BaseCommand
from main.models import *
from MyUser.models import User
import json, random

noms = ['Martin', 'Robert', 'Morel', 'Bernard', 'Lefevre', 'Fournier', 'Durand', 'Dupont', 'Blanc', 'Marchand', 'Gauthier', 'Masson', 'Fabre', 'Girard', 'Lemoine', 'Mercier', 'Moulin', 'Roux', 'Perrin', 'Leclerc']
prenoms = ['Marie', 'Julien', 'Emma', 'Pierre', 'Mathieu', 'Sarah', 'Thomas', 'Laura', 'Claire', 'Lucie', 'Jean', 'Alice', 'Maxime', 'Paul', 'Camille', 'Chloé', 'Sophie', 'Antoine', 'Benoît', 'Julie']

class Command(BaseCommand):
    help = 'Transfer data from folder to database'

    def add_arguments(self, parser):
        parser.add_argument(
            "--delete_old",
            action="store_true",
            default=False,
            help="Flag to delete old data"
        )

    def handle(self, *args, **options):
        print("Starting the data transfer process...")
        
        if options.get('delete_old'):
            print("Deleting old data...")
            Post.objects.all().delete()
            Comment.objects.all().delete()
            User.objects.all().delete()
            Like.objects.all().delete()
            Dislike.objects.all().delete()
            CommentLike.objects.all().delete()
            CommentDislike.objects.all().delete()
            print("Old data deleted.")

        print("Creating root user...")
        u, b = User.objects.get_or_create(fname="root", lname="root", email="root@rt.com")
        if b:
            u.is_superuser = True
            u.set_password("toor")
            u.save()
            print("Root user created.")
        else:
            print("Root user already exists.")

        print("Creating sample users...")
        users = []
        for i in range(len(noms)):
            u, b = User.objects.get_or_create(fname=f'{prenoms[i % len(prenoms)]}', lname=f'{noms[i]}', email=f'user{i}@us.com')
            if b:
                u.set_password("00000000")
                u.save()
                print(f"User {u.email} created.")
            users.append(u)

        print("Loading posts data from JSON file...")
        with open("data.json", "r", encoding="utf-8") as file:
            forum_data = json.load(file)
            posts = [Post.objects.get_or_create(text=i.get("text", "no text"), title=i.get("title", "no title"), user=random.choice(users))[0] for i in forum_data]
            for k in posts:
                k.save()
            print(f"{len(posts)} posts created.")

        print("Adding likes and dislikes to posts...")
        for p in posts:
            for u in users:
                s = random.choices([1, 2, 3], [50, 40, 10], k=1)[0]
                if s == 1:
                    Like.objects.get_or_create(post=p, user=u)[0].save()
                elif s == 2:
                    Dislike.objects.get_or_create(post=p, user=u)[0].save()
        print("Likes and dislikes added to posts.")

        print("Loading comments data from JSON file...")
        with open("data_comments.json", "r", encoding="utf-8") as file2:
            comment_data = json.load(file2)
            for c in comment_data:
                Comment.objects.get_or_create(post=random.choice(posts), user=random.choice(users), text=c.get("comment", "Bon poste"))[0].save()
            print(f"{len(comment_data)} comments created.")

        print("Adding likes to comments...")
        for i in Comment.objects.all():
            for u in random.choices(users, k=random.randint(5, 10)):
                try:
                    CommentLike.objects.get_or_create(comment=i, user=u)[0].save()
                except Exception:
                    continue
        print("Comment likes added.")

        print("Data transfer process completed successfully.")
