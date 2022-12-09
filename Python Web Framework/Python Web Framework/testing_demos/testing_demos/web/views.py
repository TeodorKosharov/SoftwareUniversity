from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from testing_demos.web.models import Profile


class ProfilesListView(ListView):
    template_name = 'profile-list.html'
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # context['profiles_count'] = len(Profile.objects.all())
        context['profiles_count'] = self.object_list.count()
        context['username'] = self.request.user.username
        return context


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'create.html'
    success_url = '/'
