from django.urls import path
from . import views


urlpatterns = [
    path('', views.TopicList.as_view(), name='home'),
    path('topic/<str:topic>', views.TopicDisplay.as_view(), name='topic_display'),
    path('post/add_post', views.AddPost.as_view(), name='add_post'),
    path('post/<slug:slug>', views.PostDisplay.as_view(), name="post_display"),
    path('post/like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post/edit_post/<slug:slug>', views.EditPost.as_view(), name='edit_post'),
    path('post/delete_post/<slug:slug>', views.deletePost, name='delete_post'),
    path('user_posts', views.UserPosts.as_view(), name='user_posts'),
    path('post/edit_comment/<int:pk>', views.EditComment.as_view(), name='edit_comment'),
    path('post/delete_comment/<int:comments_id>', views.deleteComment, name='delete_comment'),
    path('search', views.Search.as_view(), name="search"),
    path('contact/', views.Contact.as_view(), name='contact'),
]