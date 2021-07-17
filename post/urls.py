from django.urls import path
from .views import IndexListView, PostCreateView, PostDetailView, PostUpdateView

app_name = 'home'

urlpatterns = [
    path('', IndexListView.as_view(), name="index"),
    path('post/create', PostCreateView.as_view(), name="create"),
    path('post/<slug:slug>', PostDetailView.as_view(), name="detail"),
    path('post/edit/<slug:slug>', PostUpdateView.as_view(), name="update"),
]
