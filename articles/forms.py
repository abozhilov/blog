from django import forms
from articles import models 

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        exclude = ['publish_date', 'article']
