from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import Post,Comment,Like,Dislike,CommentLike,CommentDislike,BookMark
from .utils import human_time_difference,check_post
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


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
            'commentcount':commentc,
            'bookmarked' : BookMark.objects.filter(post=post,user=request.user).exists()
        })
    if len(posts_data)==0:
        return render(request, 'index.html', {})
    print(request.POST)
    if request.method =='POST':
        if request.user.is_authenticated:
            check_post(request)
            return HttpResponseRedirect('/')
        else:
            return redirect("mylogin")


    return render(request, 'index.html', {'posts_data': posts_data})



def Bookmarkv(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            if request.user.is_authenticated:
                check_post(request)
            else:
                return redirect("mylogin")

        try:
            bookm = BookMark.objects.get(user=request.user)
        except BookMark.DoesNotExist:
            bookm = []
        
        try:
            posts = [i.post for i in bookm]
        except TypeError:
            posts = [bookm.post]
        
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
            return render(request,"bookmark.html",{"posts_data":posts_data})
    
    else:
        return redirect("mylogin")
    

def Specif_Post(request,post_id):
    if request.method =='POST':
        if request.user.is_authenticated:
            check_post(request)
            return HttpResponseRedirect('/')
        else:
            return redirect("mylogin")
    

    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)

    
    comments_data = []
    for comment in comments:
        comments_data.append({
            'comment': comment,
            'timedelta': human_time_difference(comment.Date),
            'likes': CommentLike.objects.filter(comment=comment).count(),
            'dislikes': CommentDislike.objects.filter(comment=comment).count(),
            
        })

    result = {
        'post': post,
        'timedelta': human_time_difference(post.Date),
        'likes': Like.objects.filter(post=post).count(),
        'dislikes': Dislike.objects.filter(post=post).count(),
        'comments': comments_data,
        'commentcount':comments.count(),
        'bookmarked' : BookMark.objects.filter(post=post,user=request.user).exists()

    }
    return render(request,"post.html",{"post_data":result})
    

@login_required
def ajax_interaction(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            post_id = data.get("post_id")
            action = data.get("action")
            print(data)
            try:
                post = Post.objects.get(pk=post_id)
            except Post.DoesNotExist:
                return JsonResponse({"status": "error", "message": "Post not found"})

            if action == "upvote":
                Dislike.objects.filter(user=request.user, post=post).delete()
                Like.objects.get_or_create(user=request.user, post=post)
            elif action == "downvote":
                Like.objects.filter(user=request.user, post=post).delete()
                Dislike.objects.get_or_create(user=request.user, post=post)
            elif action == "bookmark":
                bookmark, created = BookMark.objects.get_or_create(user=request.user, post=post)
                if not created:
                    bookmark.delete()
            else:
                return JsonResponse({"status": "error", "message": "Invalid action"})

            likes = Like.objects.filter(post=post).count()
            dislikes = Dislike.objects.filter(post=post).count()
            bookmarked = BookMark.objects.filter(user=request.user, post=post).exists()
            print({
                "status": "success",
                "likes": likes,
                "dislikes": dislikes,
                "bookmarked": bookmarked,
            })
            return JsonResponse({
                "status": "success",
                "likes": likes,
                "dislikes": dislikes,
                "bookmarked": bookmarked,
            })
        except Exception as e:
            print({"status": "error", "message": f"Unexpected error: {e}"})
            return JsonResponse({"status": "error", "message": f"Unexpected error: {e}"})
    
    return JsonResponse({"status": "error", "message": "Invalid request"})