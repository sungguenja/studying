from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles
from .forms import ArticlesForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.
def index(request):
    article = Articles.objects.order_by('-pk')
    context = {
        'articles': article
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        article = ArticlesForm(request.POST)
        if article.is_valid():
            article.save()
            return redirect('accounts:index')
    else:
        article = ArticlesForm()
    context = {
        'article': article
    }
    return render(request, 'create.html', context)

def detail(request,pk):
    article = get_object_or_404(Articles, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'detail.html', context)

def update(request,pk):
    article = get_object_or_404(Articles, pk=pk)
    if request.method == 'POST':
        article = ArticlesForm(request.POST)
        if article.is_valid():
            article.save()
            return redirect('accounts:index')
    else:
        article = ArticlesForm(instance=article)
    context = {
        'article': article
    }
    return render(request, 'create.html', context)

def acc_make(request):
    if request.method == 'POST':
        article = UserCreationForm(request.POST)
        if article.is_valid():
            article.save()
            return redirect('accounts:index')
    else:
        article = UserCreationForm()
    context = {
        'article': article
    }
    return render(request, 'acc_make.html', context)