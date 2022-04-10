from django import forms
from django.forms import ModelForm
from .models import Article, Comment
#create form for making comments and writing articles

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = ('title','content','genre','excerpt', 'image')
		labels = {
		'title': 'Article Title',
		'content': 'Article Content',
		'genre': 'Select Genre',
		'excerpt': 'Short excerpt from content',
		'image': 'Cover Image'
		}
		widgets = {
		'title': forms.TextInput(attrs={'class':'form-control'}) ,
		'content': forms.Textarea(attrs={'class':'form-control', 'rows':50, 'cols':20, 'placeholder':'Allowed HTML tags are p, strong, a and br'}) ,
		'genre': forms.Select(attrs={'class':'form-control'}) ,
		'excerpt': forms.TextInput(attrs={'class':'form-control'})
		}

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('content',)
		labels = {
		'content': 'Write a comment',
		}
		widgets = {
		'content': forms.TextInput(attrs={'class':'form-control'}),
		}