from django.shortcuts import render, redirect
from online_library.web.models import Profile, Book
from online_library.web.forms import *


def get_profile():
    profile = Profile.objects.all()
    profile = profile[0] if profile else None
    return profile if profile else None


def home_page(request):
    profile = get_profile()

    if profile:
        books = Book.objects.all()
        context = {
            'profile': profile,
            'books': books
        }
        return render(request, 'home-with-profile.html', context)

    return redirect('register')


def register(request):
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


def add_book_page(request):
    profile = get_profile()

    if request.method == 'GET':
        form = AddBookForm()
    else:
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'add-book.html', context)


def edit_book_page(request, pk):
    selected_book = Book.objects.filter(pk=pk).get(pk=pk)
    profile = get_profile()
    if request.method == 'GET':
        form = EditBookForm(instance=selected_book)
    else:
        form = EditBookForm(request.POST, instance=selected_book)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'book': selected_book,
        'profile': profile
    }

    return render(request, 'edit-book.html', context)


def book_details_page(request, pk):
    selected_book = Book.objects.filter(pk=pk).get(pk=pk)
    profile = get_profile()
    context = {
        'book': selected_book,
        'profile': profile
    }

    return render(request, 'book-details.html', context)


def delete_book(request, pk):
    Book.objects.filter(pk=pk).delete()
    return redirect('home page')


def profile_page(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'profile.html', context)


def edit_profile_page(request):
    profile = get_profile()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile page')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'edit-profile.html', context)


def delete_profile_page(request):
    profile = get_profile()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile.delete()
            Book.objects.all().delete()
            return redirect('home page')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'delete-profile.html', context)
