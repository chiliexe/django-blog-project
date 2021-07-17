from crispy_forms.helper import FormHelper
from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '500px'}}))
    summary = forms.CharField(max_length=150, widget=forms.Textarea(attrs={'cols': '5', 'rows': '3'}))

    class Meta:
        model = Post
        fields = ['title', 'summary', 'content', 'image', 'category']

