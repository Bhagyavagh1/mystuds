from django.shortcuts import render

# Create your views here.
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request,'post_list.html',{'posts':posts})
    #pass              #to create function without body

from .forms import PostForm

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
        else:
            form = PostForm()
        return render(request,'post_form.html',{'form':form})