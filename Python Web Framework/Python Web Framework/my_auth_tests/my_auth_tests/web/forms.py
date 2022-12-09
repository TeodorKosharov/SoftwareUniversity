from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from my_auth_tests.web.models import Product

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username',)
        field_classes = {"username": UsernameField}

    # Скриване на допълнителната информация при регистрация
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].help_text = None


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price')
