#coding=utf-8
from django.shortcuts import render
from blog.models import BlogsPost

# Create your views here.
def index(request):
    blog_list = BlogsPost.objects.all()
    return render(request, 'index.html', {'blog_list':blog_list})