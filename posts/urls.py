from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path("<pk>/", PostDetailView.as_view(), name="detail"),
    path("", PostListView.as_view(), name="list"),
]
