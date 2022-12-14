from django.urls import path
from Posts.views import BlogHomeView, BlogPostCreate, BlogPostUpdate, BlogPostDelete, BlogPostDetail
# from django.contrib.auth.decorators import login_required

app_name = "Posts"

urlpatterns = [
    path('', BlogHomeView.as_view(), name="home"),
    path('create/', BlogPostCreate.as_view(), name="create"),
    path('edit/<str:slug>/', BlogPostUpdate.as_view(), name="edit"),
    path('delete/<str:slug>/', BlogPostDelete.as_view(), name="delete"),
    path('<str:slug>/', BlogPostDetail.as_view(), name="post"),
    # path('create/', login_required(BlogPostCreate.as_view()), name="create"),
]
