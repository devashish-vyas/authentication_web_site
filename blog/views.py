from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

post=[
    {
        'author':'Devashish Vyas',
        'title' : 'Blog Post 1',
        'content': 'First post content',
        'date_posted' : 'Aug 27 ,2018'
    },
    {
        'author':'Divy Sharma',
        'title' : 'Blog Post 2',
        'content': 'Second post content',
        'date_posted' : 'Sep 27 ,2018'
    }
]

def home(request):
    content={
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',content)



context2={
    'title':'About'
 }

def about(request):
    return render(request,'blog/about.html',context2)
