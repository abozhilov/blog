from django import forms
from captcha.fields import CaptchaField
from articles import models 

class CommentForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = models.Comment
        exclude = ['publish_date', 'article']
