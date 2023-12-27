from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'w-full py-4 px-6 border rounded-xl', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'w-full py-4 px-6 border rounded-xl', 'placeholder': 'Пароль'}))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'w-full py-4 px-6 border rounded-xl', 'placeholder': 'Имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'w-full py-4 px-6 border rounded-xl', 'placeholder': 'Электронная почта'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'w-full py-4 px-6 border rounded-xl', 'placeholder': 'Придумайте пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'w-full py-4 px-6 border rounded-xl', 'placeholder': 'Подтвердите пароль'}))
