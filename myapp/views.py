from typing import List
from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post 
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

class PostList(ListView):
    model = Post 

class PostDetail(DetailView):
    model = Post 

class EditPost(UpdateView):
    model = Post 
    fields = "__all__"

class DeletePost(DeleteView):
    model = Post 
    success_url = reverse_lazy("myapp:post-list")

class NewPost(CreateView):
    model = Post 
    fields = "__all__"

