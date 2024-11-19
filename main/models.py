from django.db import models
from MyUser.models import User
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    upVotes = models.IntegerField()
    downVotes = models.IntegerField()
    hashtags =models.CharField(max_length=1000)
    Date = models.DateTimeField(default=timezone.now)



    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    text = models.CharField(max_length=1000)
    upVotes = models.IntegerField()
    downVotes = models.IntegerField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Date = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return self.post.title +" "+ self.user.get_full_name()
