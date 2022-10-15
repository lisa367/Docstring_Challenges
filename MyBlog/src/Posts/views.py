from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from Posts.models import BlogPost
# Create your views here.


class BlogHomeView(ListView):
    model = BlogPost
    # template_name = ""
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)


class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "Posts/blogpost_create.html"
    fields = ["title", "content", ]


class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "Posts/blogpost_edit.html"
    fields = ["title", "content", "published"]


class BLogPostDelete(DeleteView):
    model = BlogPost
    template_name = "Posts/blogpost_delete.html"


