from django.contrib import admin
from .models import Post,Comment,BookMark,Like,Dislike,CommentDislike,CommentLike
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(BookMark)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(CommentLike)
admin.site.register(CommentDislike)

