from django.shortcuts import render, redirect
from gamesplay_app.web.forms import *
from gamesplay_app.web.models import Profile, Game


def get_profile():
    profile = Profile.objects.all()
    return profile[0] if profile else None


def home_page(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'home-page.html', context)


def create_profile_page(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'create-profile.html', context)


def dashboard_page(request):
    profile = get_profile()
    games = Game.objects.all()

    context = {
        'profile': profile,
        'games': games
    }

    return render(request, 'dashboard.html', context)


def create_game_page(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'create-game.html', context)


def details_game_page(request, pk):
    selected_game = Game.objects.get(pk=pk)
    profile = get_profile()

    context = {
        'profile': profile,
        'game': selected_game
    }

    return render(request, 'details-game.html', context)


def edit_game_page(request, pk):
    selected_game = Game.objects.get(pk=pk)
    profile = get_profile()

    if request.method == 'GET':
        form = EditGameForm(instance=selected_game)
    else:
        form = EditGameForm(request.POST, instance=selected_game)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'profile': profile,
        'form': form,
        'game': selected_game
    }

    return render(request, 'edit-game.html', context)


def delete_game_page(request, pk):
    selected_game = Game.objects.get(pk=pk)
    profile = get_profile()

    if request.method == 'GET':
        form = DeleteGameForm(instance=selected_game)
    else:
        form = DeleteGameForm(request.POST, instance=selected_game)
        if form.is_valid():
            selected_game.delete()
            return redirect('dashboard page')

    context = {
        'profile': profile,
        'form': form,
        'game': selected_game
    }

    return render(request, 'delete-game.html', context)


def profile_details_page(request):
    profile = get_profile()
    games = len(Game.objects.all())
    if games:
        avg_rating = sum(game.rating for game in Game.objects.all()) / games
    else:
        avg_rating = 0.0
    name = None

    if profile.first_name and profile.last_name:
        name = profile.full_name
    elif profile.first_name:
        name = profile.first_name
    elif profile.last_name:
        name = profile.last_name

    context = {
        'profile': profile,
        'name': name,
        'games': games,
        'average_rating': avg_rating
    }

    return render(request, 'details-profile.html', context)


def edit_profile_page(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details page')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'edit-profile.html', context)


def delete_profile_page(request):
    profile = get_profile()

    if request.method == 'GET':
        form = DeleteProfileForm()
    else:
        form = DeleteProfileForm(request.POST)
        if form.is_valid():
            profile.delete()
            Game.objects.all().delete()
            return redirect('home page')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'delete-profile.html', context)
