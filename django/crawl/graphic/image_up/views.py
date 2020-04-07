from django.shortcuts import render, redirect
from .models import Post
from .forms import PetFormModel
# Create your views here.
def new(request):
    if request.method == 'POST':
        form =PetFormModel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/upload/')
    else:
        form = PetFormModel()
    return render(request, 'new.html', {'form': form})

def arr(request):
    obj = Post.objects.all()
    context = {
        'title': obj.title,
        'photo': obj.photo
    }
    return render(request, 'arr.html', context)