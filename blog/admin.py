from django.contrib import admin
from .models import Article, Genre, Comment 
# Profile

# Registered models here.
@admin.register(Article)
class ArticelAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'date_posted')
	search_fields = ['title']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('commenter', 'posted_to', 'time_posted')
