from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Marvs',
        'title': 'Blog Post2',
        'content': 'Second Post Content',
        'date_posted': 'January , 2025'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': "About"})