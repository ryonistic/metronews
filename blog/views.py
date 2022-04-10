from django.shortcuts import render, redirect
from .models import Genre, Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar

# Create your views here.
def home(request):
	featured_article = Article.objects.filter(is_featured=True).order_by('-date_posted')[0]
	india_article = Article.objects.filter(genre=2).order_by('-date_posted')[0]
	banner_article = Article.objects.filter(is_banner=True).order_by('-date_posted')[0]
	genres_nav = Genre.objects.all()
	home_articles = Article.objects.filter(is_home_article=True).order_by('-date_posted')[0:5]
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	years = [2022,]
	return render(request, 'blog/home.html', {'home_articles':home_articles, 'genres_nav':genres_nav, 'months':months,'years':years, 'featured_article':featured_article,'india_article':india_article, 'banner_article':banner_article})

def about(request):
	genres_nav = Genre.objects.all()
	return render(request, 'blog/about.html', {'genres_nav':genres_nav})

def genre_view(request, genre_category):
	genre = Genre.objects.get(category=genre_category)
	articles = Article.objects.filter(genre=genre).order_by('-date_posted')
	genres_nav = Genre.objects.all()
	return render(request, 'blog/articles_by_genre.html', {'genres_nav':genres_nav,'articles':articles, 'genre':genre})


def show_article(request, slug):
	article = Article.objects.get(slug=slug)
	comments = Comment.objects.filter(posted_to=article).order_by('-time_posted')
	genres_nav = Genre.objects.all()
	if request.user.is_authenticated and request.user.is_member:
		if request.method == "POST":
			form = CommentForm(request.POST)
			if form.is_valid():
				comment = form.save(commit=False)
				comment.commenter = request.user
				comment.posted_to = article
				comment.save()
				return HttpResponseRedirect(f'/show-article/{slug}')
			else:
				messages.success(request, 'There was an error with your comment')
				return HttpResponseRedirect(f'/show-article/{slug}')

		else:
			form = CommentForm
		return render(request, 'blog/show_article.html', {'genres_nav':genres_nav,'article':article, 'form':form, 'comments':comments})
	else:
		return render(request, 'blog/show_article.html', {'genres_nav':genres_nav,'article':article, 'comments':comments})


@login_required
def article_create(request):
	if request.user.is_writer:
		if request.method == "POST":
			form = ArticleForm(request.POST, request.FILES)
			if form.is_valid():
				article = form.save(commit=False)
				article.author = request.user
				article.save()
				messages.success(request, 'Post created Successfully')
				return redirect('home')
			else:
				messages.success(request, 'There was some error in your post. Make sure you are not using (+,/,%) in the title')
				return redirect('article-create')

		else:
			form = ArticleForm
			genres_nav = Genre.objects.all()
			return render(request, 'blog/article_create.html', {'form':form, 'genres_nav': genres_nav })
	else:
		messages.success(request, 'Warning! You are not allowed on that page')
		return redirect('home')

def archive_view(request, year, month):
	month = month.capitalize()
	month_number = list(calendar.month_name).index(month)
	articles = Article.objects.filter(date_posted__year = year, date_posted__month = month_number)
	genres_nav = Genre.objects.all()
	return render(request, 'blog/archive_view.html', {'genres_nav':genres_nav, 'year':year, 'month':month, 'articles':articles})


def search_items(request):
	genres_nav = Genre.objects.all()
	if request.method=="POST":
		searched = request.POST['searched']
		articles = Article.objects.filter(title__contains=searched)
		context = {'genres_nav':genres_nav, 'searched':searched, 'articles':articles}
	else:
		context = {'genres_nav':genres_nav}
	return render(request, 'blog/search.html', context)


