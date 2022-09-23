from django.shortcuts import render

# Create your views here.
def index(request):
    base = {
        'title': 'Главная страница',
        'values': ['Главная', 'Галерея', 'Отзывы', 'Контакты']
    }
    return render(request, 'main/index.html', base)

def about(request):
    return render(request, 'main/about.html')

def gallery(request):
    return render(request, 'main/gallery.html')