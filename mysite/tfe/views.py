from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Tab


class TabList(ListView):
    model = Tab
    context_object_name = 'tabs'


class TabDetail(DetailView):
    model = Tab
    context_object_name = 'tab'
