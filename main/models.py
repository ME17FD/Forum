from django.db import models
from MyUser.models import User
from django.utils import timezone
import uuid
# Create your models here.


class Post(models.Model):
    id = models.UUIDField( primary_key = True, unique=True,
         default = uuid.uuid4,  editable = False)
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=1000)
    hashtags =models.CharField(max_length=1000,default="")
    Date = models.DateTimeField(default=timezone.now)
    user =  models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    id = models.UUIDField( primary_key = True, unique=True,
         default = uuid.uuid4,  editable = False)
    text = models.CharField(max_length=1000)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Date = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return self.post.title +" "+ self.user.get_full_name()


class BookMark(models.Model):
    Date = Date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class CommentDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
