from django.shortcuts import render, redirect
from notes_app.web.models import Profile, Note
from notes_app.web.forms import *


def get_profile():
    profile = Profile.objects.all()
    return profile[0] if profile else None


def home_page(request):
    profile = get_profile()
    notes = Note.objects.all()

    if profile:
        context = {
            'profile': profile,
            'notes': notes
        }
        return render(request, 'home-with-profile.html', context)
    return redirect('register page')


def register_page(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'home-no-profile.html', context)


def add_note_page(request):
    profile = get_profile()

    if request.method == 'GET':
        form = AddNoteForm()
    else:
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile': profile,
        'add_note': True
    }

    return render(request, 'note-create.html', context)


def edit_note_page(request, pk):
    selected_note = Note.objects.filter(pk=pk).get(pk=pk)
    profile = get_profile()

    if request.method == 'GET':
        form = EditNoteForm(instance=selected_note)
    else:
        form = EditNoteForm(request.POST, instance=selected_note)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile': profile,
        'selected_note': selected_note
    }

    return render(request, 'note-edit.html', context)


def delete_note_page(request, pk):
    selected_note = Note.objects.filter(pk=pk).get(pk=pk)
    profile = get_profile()

    if request.method == 'GET':
        form = DeleteNoteForm(instance=selected_note)
    else:
        selected_note.delete()
        return redirect('home page')

    context = {
        'form': form,
        'profile': profile,
        'selected_note': selected_note
    }

    return render(request, 'note-delete.html', context)


def note_details_page(request, pk):
    selected_note = Note.objects.filter(pk=pk).get(pk=pk)

    context = {
        'selected_note': selected_note
    }

    return render(request, 'note-details.html', context)


def profile_page(request):
    profile = get_profile()
    notes = len(Note.objects.all())

    context = {
        'profile': profile,
        'notes': notes
    }

    return render(request, 'profile.html', context)


def delete(request):
    get_profile().delete()
    Note.objects.all().delete()
    return redirect('home page')
