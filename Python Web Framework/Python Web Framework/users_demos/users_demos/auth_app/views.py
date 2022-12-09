from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from users_demos.auth_app.models import Profile

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    # Create profile variant 2
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'age')
        field_classes = {"username": UsernameField}

        # Create profile variant 1
        # Create empty profile when registering
        # def save(self, commit=True):
        #     user = super().save(commit=commit)
        #     profile = Profile(user=user)
        #
        #     if commit:
        #         profile.save()

        # variant 2
        def save(self, commit=True):
            user = super().save(commit=commit)
            first_name = self.cleaned_data['first_name']
            last_name = self.cleaned_data['last_name']
            age = self.cleaned_data['age']

            profile = Profile(
                user=user,
                first_name=first_name,
                last_name=last_name,
                age=age
            )

            if commit:
                profile.save()

        # Registration
        class SignUpView(CreateView):
            template_name = 'sign-up.html'
            form_class = SignUpForm
            success_url = reverse_lazy('index')

            # Логваме се автоматично след регистрация:
            def form_valid(self, form):
                result = super().form_valid(form)

                login(self.request, self.object)
                return result

        class SignInForm(forms.Form):
            username = forms.CharField()
            password = forms.CharField()

        # Login FBV
        def sign_in(request):
            if request.method == 'GET':
                form = SignInForm()
            else:
                form = SignInForm(request.POST)
                if form.is_valid():
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password']
                    user = authenticate(request, username=username, password=password)

                    if user:
                        login(request, user)

            context = {'form': form}

            return render(request, 'sign-in.html', context)

        # Login CBV
        class SignInView(LoginView):
            template_name = 'sign-in.html'
            success_url = reverse_lazy('index')

            # Това е единия вариант да редиректнем при успешно логване

            # def get_success_url(self):
            #     if self.success_url:
            #         return self.success_url
            #     return self.get_redirect_url() or self.get_default_redirect_url()

            # Другият вариант е чрез next променливата в темплейта

        # Logout CBV
        class SignOutView(LogoutView):
            template_name = 'sign-out.html'
