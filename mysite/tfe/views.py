from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .models import Tab


class CustomLoginView(LoginView):
    template_name = 'tfe/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tfe:tabs')


class TabList(ListView):
    model = Tab
    context_object_name = 'tabs'


class TabDetail(DetailView):
    model = Tab
    context_object_name = 'tab'


class TabCreate(CreateView):
    model = Tab
    fields = '__all__'
    success_url = reverse_lazy('tfe:tabs')


class TabUpdate(UpdateView):
    model = Tab
    fields = '__all__'
    success_url = reverse_lazy('tfe:tabs')


class TabDelete(DeleteView):
    model = Tab
    context_object_name = 'tab'
    success_url = reverse_lazy('tfe:tabs')
