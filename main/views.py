from django.shortcuts import render,HttpResponse
from .models import Post,Comment,Like,Dislike,CommentLike,CommentDislike

# Create your views here.
def home2(request):
    posts = Post.objects.prefetch_related('comment_set').all()
    return render(request, 'index.html', {'posts': posts})

def home(request):
    # Query all posts
    posts = Post.objects.all()

    # Prepare data for rendering
    posts_data = []
    for post in posts:
        # Get comments for the post
        comments = Comment.objects.filter(post=post)

        # Prepare comments with their likes/dislikes
        comments_data = []
        for comment in comments:
            comments_data.append({
                'comment': comment,
                'likes': CommentLike.objects.filter(comment=comment).count(),
                'dislikes': CommentDislike.objects.filter(comment=comment).count()
            })

        posts_data.append({
            'post': post,
            'likes': Like.objects.filter(post=post).count(),
            'dislikes': Dislike.objects.filter(post=post).count(),
            'comments': comments_data
        })

    return render(request, 'index.html', {'posts_data': posts_data})

def Bookmark(request):
    return render(request,"bookmark.html")
    

def Specif_Post(request):
    return render(request,"post.html")
    