# Here we define forms for user registration and profile updates:
# UserRegisterForm extends djangos UserCreationForm to include an additional email field.
# ProfileUpdateForm for updating a users profile allowing modifications to their profile picture and bio.

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']
