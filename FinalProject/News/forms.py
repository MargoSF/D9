from django import forms
from .models import Post, Author
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    title = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            'choice',   
            'posting_time',
            'category', 
            'post_rating',
            ]