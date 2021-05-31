from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls.base import reverse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

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


class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']#for post order newest to oldest

#<app>/<model>_<viewtype>.html


class PostDetailView(DetailView):
    model=Post


class PostCreateView(LoginRequiredMixin,CreateView): # return redirect will not work as it is a class based vuiew not a function based view
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)



class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView): # return redirect will not work as it is a class based vuiew not a function based view
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False


class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model=Post
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False


   
