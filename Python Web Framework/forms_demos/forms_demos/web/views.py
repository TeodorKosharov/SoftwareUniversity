from django import forms
from django.shortcuts import render
from forms_demos.web.models import Person
from forms_demos.web.forms import NameForm


def index(request):
    form = None
    age = None

    if request.method == 'GET':
        form = NameForm()
    elif request.method == 'POST':
        form = NameForm(
            request.POST)  # Взимаме данните от формуляра - request.POST пази данните, които потребителят е подал; request.POST връща QueryDict
        if form.is_valid():
            age = form.cleaned_data['age']  # На променливата name присвояваме стойността от полето name на формата
            Person.objects.create(age=age)  # Създаваме запис в таблицата Person

    context = {
        'form': form,
        'age': age
    }

    return render(request, 'index.html', context)


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-content'})
        }


def index_model_form(request):
    if request.method == 'GET':
        form = PersonForm()
    else:
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }

    return render(request, 'index_2.html', context)
