from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.generic import CreateView

from post.models import Post
from .forms import CommentForm
from .models import Comment


# Create your views here.


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def get_template_names(self):
        raise Http404()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        slug = self.kwargs.get('slug')
        if not self.object.name:
            self.object.name = 'anonymous'
        self.object.post = Post.objects.get(slug=slug)
        self.object.save()
        return HttpResponseRedirect(reverse('home:detail', kwargs={'slug': slug}))
