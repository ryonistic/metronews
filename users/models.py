from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from PIL import Image

class User(AbstractUser):
	is_reporter = models.BooleanField(default=False)
	is_writer = models.BooleanField(default=False)
	is_member = models.BooleanField(default=True)

	def __str__(self):
		return self.first_name+ ' ' + self.last_name

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	
	def __str__(self):
		return f'{self.user.first_name} {self.user.last_name} Profile'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
