from django.shortcuts import render, redirect
from expenses_tracker.web.models import Profile, Expense
from expenses_tracker.web.forms import *


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)

    context = {
        'profile': profile,
        'expenses': expenses,
        'budget_left': budget_left
    }

    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'GET':
        form = CreateExpenseForm()
    else:
        form = CreateExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')

    context = {'form': form}

    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditExpenseForm(instance=expense)
    else:
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('show index')

    context = {'form': form, 'expense': expense}

    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteExpenseForm(instance=expense)
    else:
        form = DeleteExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('show index')

    context = {'form': form, 'expense': expense}

    return render(request, 'expense-delete.html')


def show_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)

    context = {
        'profile': profile,
        'expenses_count': len(expenses),
        'budget_left': budget_left
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'profile-delete.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')

    context = {'form': form, 'no_profile': True}

    return render(request, 'home-no-profile.html', context)
