# Here we have Profile model to extend the functionality of the default User model with tree fields user, bio and pofile picture.
# dunder str returns username

from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    profile_picture = CloudinaryField(
        'image',
        default='default'
    )

    def __str__(self):
        return self.user.username
