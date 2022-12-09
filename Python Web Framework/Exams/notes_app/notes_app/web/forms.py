from django import forms
from notes_app.web.models import Profile, Note


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Link to Profile Image'
        }


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')
        labels = {
            'image_url': 'Link to Image'
        }


class EditNoteForm(AddNoteForm):
    pass


class DeleteNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')
        widgets = {
            'title': forms.TextInput(attrs={'disabled': True}),
            'content': forms.Textarea(attrs={'disabled': True}),
            'image_url': forms.URLInput(attrs={'disabled': True})
        }
