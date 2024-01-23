from django.urls import path

from .views import (
    Post,
    PostDetail,
    PostCreate,
    PostUpdate,
    PostDelete
)

urlpatterns = [
    path('', Post.as_view(), name='post'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/update/<int:pk>/', PostUpdate.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', PostDelete.as_view(), name='post_delete')
]