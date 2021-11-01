from django.urls import path

from .views import TabList, TabDetail

app_name = 'tfe'
urlpatterns = [
    path('', TabList.as_view(), name='tabs'),
    path('tab/<int:pk>/', TabDetail.as_view(), name='tab')
]
