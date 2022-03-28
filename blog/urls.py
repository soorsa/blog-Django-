from django.urls import path
from .views import PostListView, PostDisplayView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, PostCategory
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
#    path('categorynavbar/', Categorynav.as_view(), name='cat-navbar'),
    path('post/cat/<str:category_name>', PostCategory.as_view(), name='post-by-category'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),

]
