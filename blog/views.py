from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    allblogs = Blog.objects
    return render(request, 'blog/blogpage.html', { 'allblogs': allblogs })

def detail(request, blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blogdetail})
