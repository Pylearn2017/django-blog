import yagmail
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import CommentForm, EmailForm
from django.core.mail import send_mail

def get_promo_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            yag = yagmail.SMTP("pybot58@gmail.com","password")
            yag.send(to=data['email'],
               subject=f'Hello, its a test email from AVEAD',
               contents='This message was send by test form. Just testing..',
               )
    return redirect('home')


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

def comment_new(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
    return render(
        request, 
        'home/comment_new.html', 
         {'form':form}
        )