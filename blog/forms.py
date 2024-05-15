from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Comment

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author',None)
        self.post = kwargs.pop('post',None)
        super().__init__(*args,**kwargs)

    def save(self, commit = True):
        comment = super().save(commit = False)
        if self.author and self.post:
            comment.author = self.author
            comment.post = self.post
            if commit:
                comment.save()
            else:
                return comment

        else:
            print('Thiếu dữ liệu')

    class Meta:
        model = Comment
        fields = ["body"]