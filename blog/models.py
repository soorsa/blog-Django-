from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
	category_name = models.CharField(max_length=100, null=True, blank=True)
	creator = models.ForeignKey(User, on_delete= models.CASCADE)

	def __str__(self):
		return self.category_name

	def get_absolute_url(self):
		return reverse('post-by-category', kwargs={'pk': self.pk})


# Create your models here.
class Post(models.Model):
	"""docstring for Post"""
	advert_this = models.BooleanField(default=False)
	post_this = models.BooleanField(default=True)

	title = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete= models.CASCADE)
	#content = models.TextField()
	content = RichTextField(blank=True, null=True)
	image = models.ImageField(default= 'default.jpg', null=True, blank=True)
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	date_updated = models.DateTimeField(auto_now_add=True)
	trending_post = models.BooleanField(default=False)
	ad_title = models.CharField(max_length=100)
	ad_image = models.ImageField(default='default.jpg', null = True, blank=True)
	view_count = models.PositiveIntegerField(default = 0)



	def __str__(self):
		return self.title

	def snippet(self):
		return self.content[:300]

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete= models.CASCADE)
	author = models.CharField(max_length=100)
	content = models.TextField(max_length=200)
	created_on = models.DateTimeField(default= timezone.now)

