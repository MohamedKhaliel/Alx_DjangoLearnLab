from django.urls import path
from . import views
from .views import DetailView , CreateView , ListView


urlpatterns = [
    path('', views.home , name='home'),
    path('profile/', views.profile , name='profile'),
    path('blogs/', ListView.as_view(), name='blog'),
    path('post_list/<int:pk>/', DetailView.as_view(), name='post_detail'),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/new/', CreateView.as_view(), name='post_create'),
    path('login/', views.login_view , name='login'),
    path('logout/', views.logout_view , name='logout'),
    path('register/', views.register , name='register'),
]