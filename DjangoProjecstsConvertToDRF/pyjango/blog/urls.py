from django.urls import path
from blog import views

urlpatterns = [
    path("", views.HomeListView.as_view(), name="home"),
    path("home_detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("user-posts/<str:username>/", views.UserPostListView.as_view(), name="user-posts"),
    path("create_post/", views.CreatePostView.as_view(), name="create-post"),
    path("post_delete/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    path("post_update/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update")
]
