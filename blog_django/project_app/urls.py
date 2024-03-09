from django.urls import path
from project_app import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post'),
    path('create_post/', views.create_post, name='create_post'),
    path('post_detail/<int:post_id>', views.post_detail, name='post_detail'),
    path('tags/<tag_slug>/', views.posts_by_tag, name='posts_by_tag'),
    path('by_author/<author>/', views.posts_by_author, name='posts_by_author'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post')
]