from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Tab


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
