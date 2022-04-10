from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('genre-view/<genre_category>/', views.genre_view, name='genre_view'),
    path('show-article/<slug>/', views.show_article, name='show-article'),
    path('archive-view/<int:year>/<str:month>/', views.archive_view, name='archive-view'),
    path('article-create/',views.article_create, name='article-create'),
    path('search/',views.search_items, name='search'),
]
