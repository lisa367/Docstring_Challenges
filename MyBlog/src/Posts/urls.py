from django.urls import path
from Posts.views import BlogHomeView, BlogPostCreate, BlogPostUpdate

app_name = "Posts"

urlpatterns = [
    path('', BlogHomeView.as_view(), name="home"),
    path('create/', BlogPostCreate.as_view(), name="create"),
    path('edit/<str:slug>/', BlogPostUpdate.as_view(), name="edit"),
]
