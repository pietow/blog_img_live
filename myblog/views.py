from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'myapp/post_list.html'
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = Post
    # form_class = PostForm
    fields = '__all__'
    template_name = 'myapp/post_create.html'
    success_url = reverse_lazy('post_list')
