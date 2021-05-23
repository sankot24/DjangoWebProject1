"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog


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


class AnketaTest(forms.Form):
    name = forms.CharField(label="Полное имя", min_length = 1, max_length = 100)
    city = forms.CharField(label="Ваш регион проживания", min_length = 1, max_length = 50)

    gender = forms.ChoiceField(label="пол", 
                               choices = [('1', 'М'), ('2', 'Ж'), ('3', 'Не указывать')], 
                               widget = forms.RadioSelect, initial = 1)

    like = forms.BooleanField(label="Понравился ли вам сайт", required = False)
    
    play = forms.ChoiceField(label="Что Вам не понравилось", 
                               choices = [('1', 'Цветовая гамма'), ('2', 'Тематика блога'), ('3', 'Стиль написания текста'),
                                       ('4', 'Все перечисленное')], 
                               initial = 1)

    email = forms.CharField(label="E-mail", min_length = 1, max_length = 100, required = False)

    message = forms.CharField(label="Расскажите о проблеме", widget = forms.Textarea(attrs = {'rows':10, 'cols':80}), required = False)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {"text": "Комментарий"}


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}