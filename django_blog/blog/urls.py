from django.urls import path
from . import views
from .views import DetailView , CreateView , ListView


urlpatterns = [
    path('', views.home , name='home'),
    path('profile/', views.profile , name='profile'),
    path('blogs/', ListView.as_view(), name='blog'),
    path('post_list/<int:pk>/', DetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/new/', CreateView.as_view(), name='post_create'),
    path('login/', views.login_view , name='login'),
    path('logout/', views.logout_view , name='logout'),
    path('register/', views.register , name='register'),
    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view() , name='create_comment'),
    path('post_list/<int:post_id>/', DetailView.as_view(), name='post_detail'),
    path('posts/<int:post_id>/comments/', views.CommentListView.as_view() , name='comment_list'),
    path ('posts/<int:post_id>/comments/<int:pk>/edit', views.CommentUpdateView.as_view() , name='comment_update'),
    path ('posts/<int:post_id>/comments/<int:pk>/delete', views.CommentDeleteView.as_view() , name='comment_delete'),
]