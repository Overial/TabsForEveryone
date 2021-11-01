from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import TabList, TabDetail, TabCreate, TabUpdate, TabDelete, CustomLoginView, RegisterPageView

app_name = 'tfe'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='tfe:login'), name='logout'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('', TabList.as_view(), name='tabs'),
    path('tab/<int:pk>/', TabDetail.as_view(), name='tab'),
    path('tab_create/', TabCreate.as_view(), name='tab_create'),
    path('tab_update/<int:pk>', TabUpdate.as_view(), name='tab_update'),
    path('tab_delete/<int:pk>', TabDelete.as_view(), name='tab_delete'),
]
