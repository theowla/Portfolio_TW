from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home(request,):
    posts = Post.objects.all
    return render(request, "index.html", {'posts': posts})

def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "post.html", {'post': post}) #renders the page and gives you all the data of the Project you looked up
