from django.urls import path
from . import views

urlpatterns = [
    path('',views.reviews_home, name='reviews_home'),
    path('create', views.create, name='create'),

]