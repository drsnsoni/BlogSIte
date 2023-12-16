from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm

def index(request):
	posts = Post.objects.all()

	return render(request, 'blog/index.html', {'posts': posts})

def blog_detail(request, slug):
	post = Post.objects.get(slug=slug)
	if request.method=="POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()

			return redirect('blog_detail', slug=post.slug)

	else:
		form = CommentForm()


	return render(request, 'blog/blogdetail.html', {'post': post, 'form':form})		

