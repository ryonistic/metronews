from django.db import models
from django.utils import timezone
from django.conf import settings
#preventing special characters in the title like + / %
# from django.core.validators import RegexValidator
from django.utils.text import slugify
from PIL import Image


class Genre(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return str(self.category)


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default=1)
    excerpt = models.CharField(max_length=150, default='')
    is_featured = models.BooleanField(default=False)
    is_banner = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(blank=True, upload_to='article_images/')
    is_home_article = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        if image.height > 700 or image.width > 700:
            output_size = (700, 700)
            image.thumbnail(output_size)
            image.save(self.image.path)

    def __str__(self):
        return str(self.title)


        # def urlmaker(self):
        # 	link_made = self.title.replace(" ", "+")

        # 	return link_made

class Comment(models.Model):
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posted_to = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    time_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.commenter)
