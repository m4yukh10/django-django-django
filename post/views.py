from django.shortcuts import render, redirect
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})

def create_post(request):
    if request.method == "POST":
        name = request.POST["name"]
        heading = request.POST["heading"]
        content = request.POST["content"]
        Post.objects.create(name=name, heading=heading,content=content)
        return redirect('index')
    return render(request, "new.html")
