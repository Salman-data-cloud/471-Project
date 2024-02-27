from django.shortcuts import render

# Create your views here.

from .models import Book, Article,Podcast

def resources(request):
    books = Book.objects.all()
    articles = Article.objects.all()
    podcasts = Podcast.objects.all()
    return render(request, 'resources.html', {'books': books, 'articles': articles, 'podcasts': podcasts})