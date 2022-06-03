from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDisplay.as_view(), name="post_display"),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
