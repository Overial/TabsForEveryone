from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Tab


class TabsView(ListView):
    model = Tab
    context_object_name = 'tabs'
