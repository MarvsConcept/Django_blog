from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/<pk>', views.PostDetailView.as_view(), name='blog-home'),
    path('about/', views.about, name = 'blog-about')
]
