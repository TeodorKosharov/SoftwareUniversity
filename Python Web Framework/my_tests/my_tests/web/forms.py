from django import forms
from django.core.exceptions import ValidationError
from my_tests.web.models import *


def get_person_records():
    records = Person.objects.all()
    result = []
    id = 1
    for person_object in records:
        result.append((id, person_object))
        id += 1

    return tuple(result)


def get_available_tasks():
    records = Task.objects.all()
    result = []
    id = 1

    for task_object in records:
        result.append((id, task_object))
        id += 1

    return tuple(result)


class AddPersonForm(forms.Form):
    name = forms.CharField(max_length=20)
    age = forms.IntegerField()

    def clean_name(self):
        value = self.cleaned_data['name']
        if '_' in value:
            raise ValidationError('Underscore is invalid character!')
        return value

    def clean_age(self):
        value = self.cleaned_data['age']
        if value > 20:
            raise ValidationError('Person is too old!')
        return value


class AddTaskForm(forms.Form):
    name = forms.CharField(max_length=20)
    priority = forms.IntegerField()
    assigned_person = forms.ChoiceField(choices=get_person_records)

    def clean_priority(self):
        value = self.cleaned_data['priority']
        if value > 10:
            raise ValidationError('Priority too high!')
        return value


class ChooseTaskForm(forms.Form):
    task = forms.ChoiceField(choices=get_available_tasks)


class ChoosePersonForm(forms.Form):
    person_name = forms.ChoiceField(choices=get_person_records)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class EditPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'age')


class WidgetDemoForm(forms.Form):
    title = forms.CharField(max_length=20, label='Game title')
    score = forms.FloatField(label='Game score')
    genre = forms.CharField(max_length=20, label='Game genre')


class WidgetDemoModelForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        labels = {
            'title': 'Game title',
            'score': 'Game score',
            'genre': 'Game score'
        }


class FilesDemoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def clean_profile_picture(self):
        data = self.cleaned_data['profile_picture']
        limit = 2 * 1024 * 1024  # limit - 2MB
        if data.size > limit:
            raise ValidationError('File too large')
        return data


