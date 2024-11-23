from django.shortcuts import render,HttpResponse,redirect
from .models import Post,Comment,Like,Dislike,CommentLike,CommentDislike,BookMark
from .utils import human_time_difference
# Create your views here.

def home(request):
    # Query all posts
    posts = Post.objects.all().order_by("-Date")

    # Prepare data for rendering
    posts_data = []
    for post in posts:
        # Get comments for the post
        commentc = Comment.objects.filter(post=post).count()

        # Prepare comments with their likes/dislikes
        

        posts_data.append({
            'post': post,
            'timedelta': human_time_difference(post.Date),
            'likes': Like.objects.filter(post=post).count(),
            'dislikes': Dislike.objects.filter(post=post).count(),
            'commentcount':commentc
        })
    if len(posts_data)==0:
        return render(request, 'index.html', {})

    return render(request, 'index.html', {'posts_data': posts_data})



def Bookmarkv(request):
    if request.user.is_authenticated:
        try:
            bookm = BookMark.objects.get(user=request.user)
        except BookMark.DoesNotExist:
            bookm = []
        
        try:
            posts = [i.post for i in bookm]
        except TypeError:
            posts = [bookm.post]
        return render(request,"bookmark.html",{"posts":posts})
        
    else:
        return redirect("mylogin")
    

def Specif_Post(request,post_id):
    post = Post.objects.get(pk=post_id)
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
    return render(request,"post.html",{"post_data":result})
    