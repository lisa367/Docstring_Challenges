from django.urls import path
from Posts.views import BlogHomeView, BlogPostCreate

app_name = "Posts"

urlpatterns = [
    path('', BlogHomeView.as_view(), name="home"),
    path('create/', BlogPostCreate.as_view(), name="create"),
]
