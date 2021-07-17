from django.urls import path
from .views import ProfileListView, ProfileUpdateView

app_name = 'profile'

urlpatterns = [
    path('perfil/', ProfileListView.as_view(), name='index'),
    path('perfil/edit/<int:pk>/', ProfileUpdateView.as_view(), name='update')
]
