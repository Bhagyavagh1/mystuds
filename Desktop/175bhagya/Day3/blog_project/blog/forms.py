from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post  #for which class we want to create form
        fields = ['title','content']