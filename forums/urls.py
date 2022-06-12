from django.urls import path
from . import views


urlpatterns = [
    path('', views.TopicList.as_view(), name='home'),
    path('topic/<str:topic>', views.TopicDisplay.as_view(), name='topic_display'),
    path('post/add_post', views.AddPost.as_view(), name='add_post'),
    path('post/play', views.AddPlay.as_view(), name='play'),
    path('post/play_events', views.PlayEventsList.as_view(), name='play_events'),
    path('post/play_display/<slug:slug>', views.PlayEventsDisplay.as_view(), name='play_display'),
    path('post/edit_play/<slug:slug>', views.EditPlay.as_view(), name='edit_play'),
    path('post/delete_play/<slug:slug>', views.delete_play, name='delete_play'),
    path('post/<slug:slug>', views.PostDisplay.as_view(), name="post_display"),
    path('post/like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post/edit_post/<slug:slug>', views.EditPost.as_view(), name='edit_post'),
    path('post/delete_post/<slug:slug>', views.delete_post, name='delete_post'),
    path('user_posts', views.UserPosts.as_view(), name='user_posts'),
    path('post/edit_comment/<int:pk>', views.EditComment.as_view(), name='edit_comment'),
    path('post/delete_comment/<int:comments_id>', views.delete_comment, name='delete_comment'),
    path('post/edit_play_comment/<int:pk>', views.EditPlayComment.as_view(), name='edit_play_comment'),
    path('post/delete_play_comment/<int:comments_id>', views.delete_play_comment, name='delete_play_comment'),
    path('search', views.Search.as_view(), name="search"),
    path('contact/', views.Contact.as_view(), name='contact'),
    
]
