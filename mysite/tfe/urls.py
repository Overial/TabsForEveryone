from django.urls import path

from .views import TabsView

urlpatterns = [
    path('', TabsView.as_view(), name='tabs'),
]
