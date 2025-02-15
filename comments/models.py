from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from django.utils.timezone import now

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=now)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return f"{self.user.username} on {self.post.title}"
