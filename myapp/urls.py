from django.urls import path 
from . import views 

app_name = 'myapp'

urlpatterns = [
    path('', views.PostList.as_view(), name='post-list'),
    path('new/', views.NewPost.as_view(), name='new-post'),
    path('read/<int:pk>/', views.PostDetail.as_view(), name='read-post'),
    path('edit/<int:pk>/', views.EditPost.as_view(), name='edit-post'),
    path('delete/<int:pk>', views.DeletePost.as_view(), name='delete-post'),
]
