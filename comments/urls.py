# here im importing all functions from views and defining url paths for comments 

from django.urls import path
from .views import add_comment, edit_comment, delete_comment, like_comment

urlpatterns = [
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
    path('comment/<int:comment_id>/like/', like_comment, name='like_comment'),
]