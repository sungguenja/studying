from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles
from .forms import ArticlesForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

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

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

def login(request):
    if request.method == 'POST':
        user = AuthenticationForm(request,request.POST)
        if user.is_valid():
            auth_login(request, user.get_user())
            return redirect('accounts:index')
    else:
        user = AuthenticationForm()
    context = {
        'user': user
    }
    return render(request, 'login.html', context)