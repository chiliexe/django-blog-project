from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, When, Case, Q
from django.http import HttpResponseRedirect, Http404
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import FormMixin

from comment.forms import CommentForm
from comment.models import Comment
from .forms import PostForm
from .models import Post


# Create your views here.
class IndexListView(ListView):
    template_name = 'home/index.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 10

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     ...

    def get_queryset(self):
        query = self.request.GET.get('query')
        qs = super().get_queryset()
        qs = qs.order_by('-id')
        if query:
            qs = qs.filter(Q(title__contains=query) | Q(content__contains=query))
        qs = qs.annotate(num_comments=(Count(
            Case(When(comment__published=True, then=1))
        )))
        return qs


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'home/create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = slugify(self.object.title)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect("/")


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'home/post.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.annotate(num_comments=Count(Case(When(comment__published=True, then=1))))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comments'] = Comment.objects.filter(post=self.object)
        return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'home/edit.html'
    form_class = PostForm

    def get_initial(self):
        if not self.object.user == self.request.user:
            raise Http404
