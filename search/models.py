# defining the SearchQuery model with fields for user, query, and timestamp.
# the user field also allows guests to serch 
# dudner str returns string with username or if not authenticated Guest searched.

from django.db import models
from django.contrib.auth.models import User

class SearchQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username if self.user else 'Guest'} searched '{self.query}'"