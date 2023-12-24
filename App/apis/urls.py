from django.urls import path
from .views import BlogAPIView, BlogDetail, postCreate

urlpatterns = [
    path("", BlogAPIView.as_view(), name="blog"),
    path("<int:pk>/", BlogDetail.as_view(), name="blog_detail"),
    path("post-create/", postCreate, name="blog_create"),
]