from django.urls import path
from .views import CommentCreateView

app_name = 'comment'

urlpatterns = [
    path('create/<slug:slug>/', CommentCreateView.as_view(), name="create"),
]
