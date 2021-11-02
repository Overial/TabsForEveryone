from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

from .models import Tab


class CustomLoginView(LoginView):
    template_name = 'tfe/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tfe:tabs')


class RegisterPageView(FormView):
    template_name = 'tfe/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tfe:tabs')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPageView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tfe:tabs')
        return super(RegisterPageView, self).get(*args, **kwargs)


class TabList(LoginRequiredMixin, ListView):
    model = Tab
    context_object_name = 'tabs'
    template_name = 'tfe/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search_area') or ''

        if search_input:
            context['tabs'] = context['tabs'].filter(
                title__icontains=search_input
                # title__startswith=search_input
            )

        context['search_input'] = search_input

        return context


class TabDetail(LoginRequiredMixin, DetailView):
    model = Tab
    fields = '__all__'
    context_object_name = 'tab'


class TabCreate(LoginRequiredMixin, CreateView):
    model = Tab
    fields = ['band', 'album', 'title', 'instrument', 'description']
    success_url = reverse_lazy('tfe:tabs')


class TabUpdate(LoginRequiredMixin, UpdateView):
    model = Tab
    fields = '__all__'
    success_url = reverse_lazy('tfe:tabs')


class TabDelete(LoginRequiredMixin, DeleteView):
    model = Tab
    context_object_name = 'tab'
    success_url = reverse_lazy('tfe:tabs')
