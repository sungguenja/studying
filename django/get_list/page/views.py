from django.shortcuts import render

# Create your views here.
def testing(request):
    if request.method == 'POST':
        print(request.POST.getlist('test'))
    return render(request,'test.html')