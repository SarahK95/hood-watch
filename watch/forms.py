from django import forms
from .models import Business,Profile,Post,Comment


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['username','hood','image']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['owner','hoody']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']