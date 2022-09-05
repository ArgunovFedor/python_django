from django import forms
from app_blog import models


class BlogForm(forms.ModelForm):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = models.Blog
        fields = ('name', 'description')
