from django.urls import path
from .views import IndexListView

app_name = 'category'

urlpatterns = [
    path('<str:name>/', IndexListView.as_view(), name='index')
]
