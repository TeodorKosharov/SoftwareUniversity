from django import forms
from my_music_app.web.models import Profile, Album
from django.forms import TextInput


class RegisterProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image_url', 'price')
        labels = {
            'name': 'Album Name',
            'image_url': 'Image URL'
        }


class EditAlbumForm(AddAlbumForm):
    pass


class DeleteAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image_url', 'price')
        labels = {
            'name': 'Album Name',
            'image_url': 'Image URL'
        }
        widgets = {
            'name': TextInput(attrs={'readonly': True}),
            'artist': TextInput(attrs={'readonly': True}),
            'genre': TextInput(attrs={'readonly': True}),
            'description': TextInput(attrs={'readonly': True}),
            'image_url': TextInput(attrs={'readonly': True}),
            'price': TextInput(attrs={'readonly': True}),
        }


class DeleteProfileForm(forms.Form):
    pass
