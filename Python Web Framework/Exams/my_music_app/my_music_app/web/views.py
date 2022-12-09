from django.shortcuts import render, redirect
from my_music_app.web.models import Profile, Album
from my_music_app.web.forms import *


def get_profile():
    profile = Profile.objects.all()
    return profile[0] if profile else None


def home(request):
    profile = get_profile()
    if profile:
        return redirect('logged in')
    return redirect('register user')


def register_page(request):
    if request.method == 'GET':
        form = RegisterProfileForm()
    else:
        form = RegisterProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logged in')

    context = {
        'form': form
    }

    return render(request, 'home-no-profile.html', context)


def logged_in(request):
    profile = get_profile()
    albums = Album.objects.all()

    context = {
        'profile': profile,
        'albums': albums
    }

    return render(request, 'home-with-profile.html', context)


def add_album_page(request):
    if request.method == 'GET':
        form = AddAlbumForm()
    else:
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile': get_profile()
    }

    return render(request, 'add-album.html', context)


def details_album_page(request, pk):
    selected_album = Album.objects.get(pk=pk)

    context = {
        'album': selected_album,
        'profile': get_profile()
    }

    return render(request, 'album-details.html', context)


def edit_album_page(request, pk):
    selected_album = Album.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditAlbumForm(instance=selected_album)
    else:
        form = EditAlbumForm(request.POST, instance=selected_album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'album': selected_album,
        'profile': get_profile()
    }

    return render(request, 'edit-album.html', context)


def delete_album_page(request, pk):
    selected_album = Album.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteAlbumForm(instance=selected_album)
    else:
        form = DeleteAlbumForm(request.POST, instance=selected_album)
        if form.is_valid():
            selected_album.delete()
            return redirect('home page')

    context = {
        'form': form,
        'album': selected_album,
        'profile': get_profile()
    }

    return render(request, 'delete-album.html', context)


def profile_details_page(request):
    user = get_profile()
    albums = len(Album.objects.all())

    context = {
        'user': user,
        'albums': albums,
        'profile': get_profile()
    }

    return render(request, 'profile-details.html', context)


def profile_delete_page(request):
    if request.method == 'GET':
        form = DeleteProfileForm()
    else:
        form = DeleteProfileForm(request.POST)
        if form.is_valid():
            get_profile().delete()
            Album.objects.all().delete()
            return redirect('home page')

    context = {
        'form': form,
        'profile': get_profile()
    }

    return render(request, 'profile-delete.html', context)
