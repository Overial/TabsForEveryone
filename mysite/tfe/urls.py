from django.urls import path

from .views import TabList, TabDetail, TabCreate, TabUpdate

app_name = 'tfe'
urlpatterns = [
    path('', TabList.as_view(), name='tabs'),
    path('tab/<int:pk>/', TabDetail.as_view(), name='tab'),
    path('tab_create/', TabCreate.as_view(), name='tab_create'),
    path('tab_update/<int:pk>', TabUpdate.as_view(), name='tab_update'),
]
