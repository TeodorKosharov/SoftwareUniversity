from django import forms
from gamesplay_app.web.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image_url', 'summary')
        labels = {
            'max_level': 'Max Level',
            'image_url': 'Image URL'
        }


class EditGameForm(CreateGameForm):
    pass


class DeleteGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image_url', 'summary')
        labels = {
            'max_level': 'Max Level',
            'image_url': 'Image URL'
        }
        widgets = {
            'title': forms.TextInput(attrs={'readonly': True}),
            'category': forms.TextInput(attrs={'readonly': True}),
            'rating': forms.NumberInput(attrs={'readonly': True}),
            'max_level': forms.NumberInput(attrs={'readonly': True}),
            'image_url': forms.URLInput(attrs={'readonly': True}),
            'summary': forms.Textarea(attrs={'readonly': True}),
        }


class EditProfileForm(CreateProfileForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password', 'first_name', 'first_name', 'last_name', 'profile_picture')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture'
        }


class DeleteProfileForm(forms.Form):
    pass
