from django.core.management.base import BaseCommand
import random,os,string
import time
from main.models import *
from django.core.files import File
from PIL import Image


class Command(BaseCommand):
    help = 'Transfer data from folder to database'

    


    def handle(self, *args, **options):
        try:
            # Creating example users (you can customize this part based on your User model)
            user1 = User.objects.create(phone="phone", email="user1@example.com", fname="John", lname="Doe")
            user2 = User.objects.create(phone="phone", email="user2@example.com", fname="Jane", lname="Smith")
        except Exception as e:
            user1 = User.objects.get(email="user1@example.com")
            user2 = User.objects.get(email="user2@example.com")
        # Creating 5 example posts
        posts = [
            Post.objects.create(title="Post 1", text="This is the first post.", hashtags="#example #first",user=user1),
            Post.objects.create(title="Post 2", text="This is the second post.", hashtags="#example #second",user=user2),
            Post.objects.create(title="Post 3", text="This is the third post.", hashtags="#example #third",user=user1),
            Post.objects.create(title="Post 4", text="This is the fourth post.", hashtags="#example #fourth",user=user1),
            Post.objects.create(title="Post 5", text="This is the fifth post.", hashtags="#example #fifth",user=user1)
        ]
        
        # Creating comments for the posts
        comments = [
            Comment.objects.create(text="Great post!", post=posts[0], user=user1),
            Comment.objects.create(text="Nice read, thanks for sharing!", post=posts[0], user=user2),
            Comment.objects.create(text="Interesting points. I agree with most of them.", post=posts[0], user=user1),
            Comment.objects.create(text="I love this topic!", post=posts[1], user=user2)
        ]
        
        # Populating likes and dislikes for posts
        Like.objects.create(user=user1, post=posts[0])
        Dislike.objects.create(user=user2, post=posts[1])
        Like.objects.create(user=user2, post=posts[3])
        Dislike.objects.create(user=user1, post=posts[4])
        
        # Populating likes and dislikes for comments
        CommentLike.objects.create(user=user1, comment=comments[0])
        CommentDislike.objects.create(user=user2, comment=comments[1])
        CommentLike.objects.create(user=user2, comment=comments[2])
        CommentDislike.objects.create(user=user1, comment=comments[3])

        print("Dummy data populated successfully!")
            
            
            
