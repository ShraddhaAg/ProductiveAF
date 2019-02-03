from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from accounts.models import Profile, Intrest, Keywords
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileDetail(LoginRequiredMixin, generic.DetailView):
    login_url='/accounts/login'
    model = Profile

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        id = self.kwargs.get('pk', self.request.user.id)
        return queryset.filter(id=id).get()

# @login_required(login_url='/accounts/login')
# class ProfileCreate(CreateView):
#     model = Profile
#     fields = '__all__'
#     success_url = reverse_lazy('profile')

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    login_url='/accounts/login'
    model = Profile
    fields = ['name','email_id', 'notification_time', 'intrests']
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        id = self.kwargs.get('pk', self.request.user.id)
        return queryset.filter(id=id).get()
#
# @login_required(login_url='/accounts/login')
# class ProfileDelete(DeleteView):
#     model = Profile
#     success_url = reverse_lazy('profile')

class KeywordList(generic.ListView):
    model = Keywords
