from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse 
from .forms import CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View
from django.contrib.auth.models import User
from .models import Post, Comment, Category
from django.urls import reverse

# Create your views here.
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

#class Categorynav(ListView):
#	model = Category
#	template_name = 'blog/categorynavbar.html'
#	context_object_name = 'catnavitem'
		

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 3

	#def get_context_data(self, **kwargs):
	#	context = super(PostCategory, self).get_context_data(**kwargs)
	#	context['category'] = self.category
	#	return context

	def get_context_data(self, **kwargs):
		cat_item = Category.objects.all()
		title = 'The Rosy Iyke Blog'
		context = super(PostListView, self).get_context_data(**kwargs)
		context['cat_item'] = cat_item
		context['title'] = title
		return context

class PostCategory(ListView):
	model = Post
	template_name = 'blog/post_category.html'
	context_object_name = 'posts'


	def get_queryset(self):
		category = get_object_or_404(Category, category_name=self.kwargs.get('category_name'))
		return Post.objects.filter(category=category)

	def get_context_data(self, **kwargs):
		cat_item = Category.objects.all()
		title = 'The Rosy Iyke Blog'
		context = super(PostCategory, self).get_context_data(**kwargs)
		context['cat_item'] = cat_item
		context['title'] = title
		return context


class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

	def get_context_data(self, **kwargs):
		cat_item = Category.objects.all()
		title = 'The Rosy Iyke Blog'
		context = super(UserPostListView, self).get_context_data(**kwargs)
		context['cat_item'] = cat_item
		context['title'] = title
		return context


class PostDetailView(View):
	model = Post
	"""docstring for PostDisplayView"""
	def get(self, request, *args, **kwargs):
		view = PostDisplayView.as_view()
		return view(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		view = CommentFormView.as_view()
		return view(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		cat_item = Category.objects.all()
		context = super(PostDetailView, self).get_context_data(**kwargs)
		context['cat_item'] = cat_item
		return context
		

class PostDisplayView(DetailView):
	model = Post

	def get_object(self):
		object= super(PostDisplayView, self).get_object()
		object.view_count += 1
		object.save()
		return object

	def get_context_data(self, **kwargs):
		cat_item = Category.objects.all()
		context = super(PostDisplayView, self).get_context_data(**kwargs)
		context['cat_item'] = cat_item
		context['comments'] = Comment.objects.filter(post=self.get_object())
		context['form'] = CommentForm
		return context

class CommentFormView(FormView):
	form_class = CommentForm
	template_name = 'blog/post_detail.html'

	def form_valid(self, form):
	#	form.instance.author = self.request.user
		post = Post.objects.get(pk=self.kwargs['pk'])
		form.instance.post = post
		form.save()
		return super(CommentFormView, self).form_valid(form)

	def get_success_url(self, **kwargs):
		return reverse('post-detail', kwargs={'pk': self.kwargs['pk']})

	 
class PostCreateView(LoginRequiredMixin, UserPassesTestMixin,CreateView):
	model = Post
	fields = ['advert_this', 'post_this', 'title', 'category', 'content', 'image', 'trending_post', 'ad_title', 'ad_image' ]


	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	#def test_func(self):
	#	if self.request.user.is_staff:
	#		return True
	#	return False

	def get_context_data(self, **kwargs):
		cat_item = Category.objects.all()
		title = 'Create a Post'
		context = super(PostCreateView, self).get_context_data(**kwargs)
		context['cat_item'] = cat_item
		context['title'] = title
		return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['advert_this', 'post_this', 'title', 'category', 'content', 'image', 'trending_post', 'ad_title', 'ad_image' ]

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

		#if self.request.user.is_staff:
		#	return True
		#return False

	def get_context_data(self, **kwargs):
		cat_item = Category.objects.all()
		title = 'Update a Post'
		context = super(PostUpdateView, self).get_context_data(**kwargs)
		context['cat_item'] = cat_item
		context['title'] = title
		return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

		#if self.request.user.is_staff:
		#	return True
		#return False

#class About(View):
#	model = Post
#	template_name = 'blog/about.html'
#	context_object_name = 'posts'


def about(request):
	context = {
		'posts': Post.objects.all(),
		'title': 'About Us'
	}
	return render(request, 'blog/about.html', context)

def contact(request):
	context = {
		'posts': Post.objects.all(),
		'title': 'Contact Us'
		}
	return render(request, 'blog/contact.html', context)


