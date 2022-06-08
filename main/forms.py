from django import forms
from django.forms import ModelForm

from main.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']
