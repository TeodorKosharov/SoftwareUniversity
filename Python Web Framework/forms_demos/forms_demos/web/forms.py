from django import forms


class NameForm(forms.Form):
    GENDER_OPTIONS = (
        (1, 'Male'),
        (2, 'Female'),
    )

    age = forms.CharField(
        max_length=30,
        widget=forms.Textarea(attrs={'placeholder': 'Enter your age'})
    )
    gender = forms.ChoiceField(choices=GENDER_OPTIONS, widget=forms.RadioSelect)
