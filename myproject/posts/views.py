from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms


def posts_list(req):
    posts = Post.objects.all().order_by('-date')
    return render(req, 'posts/posts_list.html', {'posts': posts})

def post_page(req, slug):
    post = Post.objects.get(slug=slug)
    return render(req, 'posts/post_page.html', {'post': post})

@login_required(login_url="/users/login/")
def post_new(req):
    if req.method == 'POST':
        form = forms.CreatePost(req.POST, req.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = req.user
            newpost.save()
            return redirect('posts:list')

    else:
        form = forms.CreatePost()
    return render(req, 'posts/post_new.html', {'form': form})