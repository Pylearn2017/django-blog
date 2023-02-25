from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class EmailForm(forms.Form):
    email = forms.EmailField()
    