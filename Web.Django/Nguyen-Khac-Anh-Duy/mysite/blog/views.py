from django.shortcuts import render
from .models import Post, login
# Create your views here.
def list(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blogs/blogs.html', Data)

def post(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'blogs/post.html' , {'post': post})