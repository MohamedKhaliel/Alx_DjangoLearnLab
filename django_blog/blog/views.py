from django.shortcuts import render , redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
from .forms import SignUpForm , LoginForm , ProfileForm , PostForm
from django.views.generic import ListView , DetailView , CreateView ,UpdateView , DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request , 'blog/base.html')

def register(request):
    if request.method == "POST" :
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , 'registered successfully')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request , 'blog/register.html' , {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username , password = password)
            if user is not None:
                login(request , user)
                return redirect('home')
            else:
                messages.error(request , 'invalid credentials')
                return redirect('login')
    else:
        form = LoginForm()
    return render(request , 'blog/login.html' , {'form':form})

def logout_view(request):
    logout(request)
    messages.success(request , "Logged out successfully!")
    return redirect('login')


def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST , instance = user)
        if form.is_valid():
            form.save()
            messages.success(request , 'profile updated successfully')
            return redirect('profile')
    else:
        form = ProfileForm(instance = user)
    return render(request , 'blog/profile.html' , {'form':form})

class CreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog')
    
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ListView(ListView):
    model = Post
    template_name = 'blog/blogs.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.all()
    
class DetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        return Post.objects.filter(id = self.kwargs['pk'])
    


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']  # Fields to display in the form
    template_name = 'blog/post_update.html'  # Template for the update form
    success_url = reverse_lazy('blog')  # Redirect to post list after successful update

    def form_valid(self, form):
        """
        Additional logic (if needed) before saving the form.
        """
        form.instance.author = self.request.user  # Ensure the author remains the same
        return super().form_valid(form)

    def test_func(self):
        """
        Restrict access to the original author of the post.
        """
        post = self.get_object()
        return post.author == self.request.user
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # Template for confirmation
    success_url = reverse_lazy('blog')  # Redirect to the post list after deletion

    def test_func(self):
        """
        Restrict delete access to the author of the post.
        """
        post = self.get_object()
        return post.author == self.request.user  