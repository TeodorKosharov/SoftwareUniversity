from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from django import forms

from forms_demos_2.web.models import Todo, Person


def validate_text(value):
    if '_' in value:
        raise ValidationError('underscore is invalid character')


# Base Form:
class TodoForm(forms.Form):
    text = forms.CharField()
    is_done = forms.BooleanField(required=False)

    def clean_text(self):
        data = self.cleaned_data['text']
        if '_' in data:
            raise ValidationError('underscore is invalid character')


# ModelForm:
class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

    def clean_text(self):
        return self.cleaned_data['text'].lower()


# ModelForm Media Files:
class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


# Base Form validation demos:
def index(request):
    if request.method == 'GET':
        form = TodoForm()
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            return HttpResponse('All is valid')

    context = {
        'form': form
    }

    return render(request, 'index.html', context)


# ModelForm validation demos:
def index_2(request):
    if request.method == 'GET':
        form = TodoCreateForm()
    else:
        form = TodoCreateForm(request.POST)
        form.save()
        if form.is_valid():
            return HttpResponse('All is valid')

    context = {
        'form': form
    }

    return render(request, 'index_2.html', context)


# ModelForm Media Files demos:
def index_3(request):
    if request.method == 'GET':
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    person = Person.objects.get(pk=6)

    context = {
        'form': form,
        'person': person
    }

    return render(request, 'index_3.html', context)
