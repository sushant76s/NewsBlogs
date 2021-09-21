from django.shortcuts import render, HttpResponse
from .models import Blog
from django.conf import settings
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    context = {
        "sushant":"this is the variable"
    }
    return render(request, 'index.html', context)
    return HttpResponse("this is homepage")
# def about(request):
#     return HttpResponse("this is about page")


def blogs(request):
    blogPost = Blog.objects.all()
    paginator = Paginator(blogPost, 5)
    blog_num = request.GET.get('page')
    blog_obj = paginator.get_page(blog_num)
    return render(request, "blog.html", {'blog_obj': blog_obj})

def contact(request):
    return render(request, 'contact.html')
