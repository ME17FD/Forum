from django.shortcuts import render,HttpResponse,redirect
from .models import Post,Comment,Like,Dislike,CommentLike,CommentDislike
from .utils import human_time_difference
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
                'timedelta': human_time_difference(comment.Date),
                'likes': CommentLike.objects.filter(comment=comment).count(),
                'dislikes': CommentDislike.objects.filter(comment=comment).count()
            })

        posts_data.append({
            'post': post,
            'timedelta': human_time_difference(post.Date),
            'likes': Like.objects.filter(post=post).count(),
            'dislikes': Dislike.objects.filter(post=post).count(),
            'comments': comments_data
        })

    return render(request, 'index.html', {'posts_data': posts_data})

def Bookmark(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request,"bookmark.html",{"posts":posts})
    else:
        return redirect("login")
    

def Specif_Post(request,pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    
    comments_data = []
    for comment in comments:
        comments_data.append({
            'comment': comment,
            'timedelta': human_time_difference(comment.Date),
            'likes': CommentLike.objects.filter(comment=comment).count(),
            'dislikes': CommentDislike.objects.filter(comment=comment).count()
        })

    result = {
        'post': post,
        'timedelta': human_time_difference(post.Date),
        'likes': Like.objects.filter(post=post).count(),
        'dislikes': Dislike.objects.filter(post=post).count(),
        'comments': comments_data
    }
    return render(request,"post.html",result)
    