from .models import Image, Profile, Follow, Comment
from django.forms import ModelForm


class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["created", "account_holder", "followers", "following"]

