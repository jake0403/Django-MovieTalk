from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_api/', views.get_api, name='get_api'),
    path('genres/<int:genre_id>', views.get_movies, name='get_movies'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('recommend/', views.recommend, name='recommend'),
    path('search/', views.search, name='search'),
]
