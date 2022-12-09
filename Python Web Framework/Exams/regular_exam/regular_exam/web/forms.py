from django import forms
from regular_exam.web.models import Profile, Car


class RegisterProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'model', 'year', 'image_url', 'price')
        labels = {
            'image_url': 'Image URL'
        }


class EditCarForm(CreateCarForm):
    pass


class DeleteCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'model', 'year', 'image_url', 'price')
        labels = {
            'image_url': 'Image URL'
        }
        widgets = {
            'type': forms.TextInput(attrs={'disabled': True}),
            'model': forms.TextInput(attrs={'disabled': True}),
            'year': forms.NumberInput(attrs={'disabled': True}),
            'image_url': forms.URLInput(attrs={'disabled': True}),
            'price': forms.NumberInput(attrs={'disabled': True}),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture'
        }


class DeleteProfileForm(forms.Form):
    pass
