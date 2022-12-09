from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField, UserCreationForm

UserModel = get_user_model()


class RegForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')
        field_classes = {"username": UsernameField}
