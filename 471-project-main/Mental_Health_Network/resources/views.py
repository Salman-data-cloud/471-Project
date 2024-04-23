
from django.shortcuts import render
from .models import Book, Article,Podcast


def resources(request):
    return render(request, 'resources.html')

def books_page(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})
def podcasts_page(request):
    podcasts = Podcast.objects.all()
    return render(request, 'podcasts.html', {'podcasts': podcasts})
def articles_page(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})