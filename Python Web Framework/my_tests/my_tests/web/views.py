from django.http import HttpResponse
from django.shortcuts import render
from my_tests.web.forms import *
from my_tests.web.models import *


def create_model_form(request, form_class):
    if request.method == 'GET':
        form = form_class()
    else:
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
    return form


def form1(request):
    if request.method == 'GET':
        form = AddPersonForm()
    else:
        form = AddPersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            Person.objects.create(name=name, age=age)
            return HttpResponse('Record created successfully!')

    context = {
        'form': form,
    }

    return render(request, 'form_1.html', context)


def form2(request):
    if request.method == 'GET':
        form = AddTaskForm()
    else:
        form = AddTaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            priority = form.cleaned_data['priority']
            assigned_to_person_id = form.cleaned_data['assigned_person']
            person_object = Person.objects.get(pk=assigned_to_person_id)
            Task.objects.create(name=name, priority=priority, assigned_to=person_object)
            return HttpResponse(f'Record created successfully!')

    context = {
        'form': form
    }

    return render(request, 'form_2.html', context)


def check_tasks(request):
    assigned_to = None

    if request.method == 'GET':
        form = ChooseTaskForm()
    else:
        form = ChooseTaskForm(request.POST)
        if form.is_valid():
            task_id = int(form.cleaned_data['task'])
            task = [task for task in Task.objects.all() if task.id == task_id][0]
            assigned_to = task.assigned_to

    context = {
        'form': form,
        'assigned_person': assigned_to
    }

    return render(request, 'check_tasks.html', context)


def count_tasks(request):
    tasks = None
    person_name = None

    if request.method == 'GET':
        form = ChoosePersonForm()
    else:
        form = ChoosePersonForm(request.POST)
        if form.is_valid():
            person_id = int(form.cleaned_data['person_name'])
            tasks = len([task for task in Task.objects.all() if task.assigned_to.id == person_id])
            person_name = [person for person in Person.objects.all() if person.pk == person_id][0].name

    context = {
        'form': form,
        'tasks': tasks,
        'person_name': person_name
    }

    return render(request, 'count_tasks.html', context)


def students(request):
    form = create_model_form(request, StudentForm)

    context = {
        'form': form
    }

    return render(request, 'students.html', context)


def pets(request):
    form = create_model_form(request, PetForm)

    context = {
        'form': form
    }

    return render(request, 'pets.html', context)


def edit_person(request):
    last_person = list(Person.objects.all())[-1]
    if request.method == 'GET':
        form = EditPersonForm(instance=last_person)
    else:
        form = EditPersonForm(request.POST, instance=last_person)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }

    return render(request, 'edit_person.html', context)


def widgets_demo(request):
    if request.method == 'GET':
        form = WidgetDemoForm()
    else:
        form = WidgetDemoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            score = form.cleaned_data['score']
            genre = form.cleaned_data['genre']
            Game.objects.create(title=title, score=score, genre=genre)

    context = {
        'form': form
    }

    return render(request, 'widgets_demo.html', context)


def widgets_demo2(request):
    if request.method == 'GET':
        form = WidgetDemoModelForm()
    else:
        form = WidgetDemoModelForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }

    return render(request, 'widgets_demo2.html', context)


def mediafiles_demo(request):
    if request.method == 'GET':
        form = FilesDemoForm()
    else:
        form = FilesDemoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }

    return render(request, 'mediafile_demo.html', context)
