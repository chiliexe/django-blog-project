from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.contrib.auth.admin import User
from post.models import Post
from django.db.models import Count, Case, When

from userprofile.forms import UserForm


class ProfileListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'profile/index.html'

    def get_context_data(self, **kwargs):
        cx = super().get_context_data()
        cx['posts'] = Post.objects\
            .annotate(num_comments=Count(Case(When(comment__published=True, then=1))))\
            .filter(user=self.request.user)
        return cx


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'profile/editprofile.html'
    success_url = reverse_lazy('profile:index')

    def get_initial(self):
        pk = self.kwargs.get('pk')
        user = User.objects.get(pk=pk)
        if not self.object == self.request.user:
            raise Http404
