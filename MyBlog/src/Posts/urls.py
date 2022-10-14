from django.urls import path
from Posts.views import BlogHomeView

app_name = "Posts"

urlpatterns = [
    path('', BlogHomeView.as_view(), name="home"),
]
