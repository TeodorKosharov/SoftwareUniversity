from django.shortcuts import render, redirect
from regular_exam.web.models import Profile, Car
from regular_exam.web.forms import *


def get_profile():
    profile = Profile.objects.all()
    return profile[0] if profile else None


def index_page(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'index.html', context)


def profile_create_page(request):
    profile = get_profile()
    if request.method == 'GET':
        form = RegisterProfileForm()
    else:
        form = RegisterProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile-create.html', context)


def catalogue_page(request):
    profile = get_profile()
    cars = Car.objects.all()
    total_cars = len(cars)

    context = {
        'profile': profile,
        'cars': cars,
        'total_cars': total_cars
    }

    return render(request, 'catalogue.html', context)


def car_create_page(request):
    profile = get_profile()

    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'car-create.html', context)


def car_details_page(request, pk):
    profile = get_profile()
    selected_car = Car.objects.get(pk=pk)

    context = {
        'profile': profile,
        'car': selected_car
    }

    return render(request, 'car-details.html', context)


def car_edit_page(request, pk):
    profile = get_profile()
    selected_car = Car.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditCarForm(instance=selected_car)
    else:
        form = EditCarForm(request.POST, instance=selected_car)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    context = {
        'profile': profile,
        'form': form,
        'car': selected_car
    }

    return render(request, 'car-edit.html', context)


def car_delete_page(request, pk):
    profile = get_profile()
    selected_car = Car.objects.get(pk=pk)

    if request.method == 'GET':
        form = DeleteCarForm(instance=selected_car)
    else:
        form = DeleteCarForm(instance=selected_car)
        selected_car.delete()
        return redirect('catalogue page')

    context = {
        'profile': profile,
        'form': form,
        'car': selected_car
    }

    return render(request, 'car-delete.html', context)


def profile_details_page(request):
    profile = get_profile()
    name = profile.full_name
    total_cars_price = sum([car.price for car in Car.objects.all()])

    context = {
        'profile': profile,
        'full_name': name,
        'total_cars_price': total_cars_price
    }

    return render(request, 'profile-details.html', context)


def profile_edit_page(request):
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

    return render(request, 'profile-edit.html', context)


def profile_delete_page(request):
    profile = get_profile()

    if request.method == 'GET':
        form = DeleteProfileForm()
    else:
        Car.objects.all().delete()
        profile.delete()
        return redirect('index page')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile-delete.html', context)
