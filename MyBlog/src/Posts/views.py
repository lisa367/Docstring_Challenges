from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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


@method_decorator(login_required, name='dispatch')
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "Posts/blogpost_create.html"
    fields = ["title", "content", "created_on", ]


@method_decorator(login_required, name='dispatch')
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "Posts/blogpost_edit.html"
    fields = ["title", "content", "published"]


@method_decorator(login_required, name='dispatch')
class BlogPostDelete(DeleteView):
    model = BlogPost
    # template_name = "Posts/blogpost_delete.html"
    success_url = reverse_lazy("Posts:home")
    context_object_name = "post"


class BlogPostDetail(DetailView):
    model = BlogPost
    # template_name = "Posts/blogpost_detail.html"
    context_object_name = "post"


