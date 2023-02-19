from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Comment

# Create your views here.
def home_page(request):
    posts = Post.objects \
        .filter(published_date__lte=timezone.now()) \
        .order_by('published_date')
    return render(
        request, 
        'home/post_list.html', 
        {'posts':posts}
        )

def post_detail(request, pk):
    obj = {}
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    obj['post'] = post
    obj['comments'] = comments

    return render(
        request, 
        'home/post_detail.html', 
        {'obj':obj}
        )
