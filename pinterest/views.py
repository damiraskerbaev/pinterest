from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView
)

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Pinterest

class Post(ListView):
    model = Pinterest
    template_name = 'pinterest/post.html'
    context_object_name = 'post'

class PostDetail(DetailView):
    model = Post
    template_name = 'pinterest/post-detail.html'
    context_object_name = 'post'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'book/book-create.html'
    context_object_name = 'post-create'
    fields = (
        'name',
        'description',
        'released_date',
        'cover'
    )

    success_url = reverse_lazy('post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdate(UpdateView):
    model = Post
    template_name = 'post/post-update.html'
    context_object_name = 'post_update'
    fields = {
        'name',
        'description',
        'cover'
    }

    success_url = reverse_lazy('post')


class PostDelete(DeleteView):
    model = Post
    template_name = 'post/post-delete.html'
    context_object_name = 'post_delete'
    success_url = reverse_lazy('post')

