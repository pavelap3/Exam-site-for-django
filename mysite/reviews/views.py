from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
# Create your views here.

def reviews_home(request):
    reviews = Articles.objects.order_by('-date')
    return render(request, 'reviews/reviews_home.html', {'reviews': reviews})

def create(request):
    error = ' '
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не заполнена'


    form = ArticlesForm()

    data ={
        'form':form,
        'error':error
    }

    return render(request, 'reviews/create.html', data)