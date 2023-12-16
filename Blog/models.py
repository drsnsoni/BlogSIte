from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=50)
	intro = models.TextField()
	body = models.TextField()
	date_added = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ['-date_added']


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)
	body = models.TextField()
	date_added = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ['-date_added']
