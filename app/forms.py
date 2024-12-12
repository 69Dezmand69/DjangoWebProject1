"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from .models import Comment
from .models import Blog
from .models import VideoGame

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

    
   

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя пользователя'
        })
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Пароль'
        })
    )

class FeedbackForm(forms.Form):
    nickname = forms.CharField(label='Никнейм',max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    game = forms.CharField(label='Какую игру приобрели',max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    speed = forms.ChoiceField(label='Скорость (от 1 до 5)',choices=[(i, str(i)) for i in range(1, 6)],required=True,widget=forms.Select(attrs={'class': 'form-control'}))
    price = forms.ChoiceField(label='Цена (от 1 до 5)',choices=[(i, str(i)) for i in range(1, 6)],required=True,widget=forms.Select(attrs={'class': 'form-control'}))
    service = forms.ChoiceField(label='Качество обслуживания (от 1 до 5)',choices=[(i, str(i)) for i in range(1, 6)],required=True,widget=forms.Select(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Комментарий',required=True,widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image')
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}




class VideoGameForm(forms.ModelForm):
    class Meta:
        model = VideoGame
        fields = ['title', 'description', 'image', 'genres', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'genres': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }