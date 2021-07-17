from django.views.generic import ListView
from .models import Category
from post.models import Post

# Create your views here.


class IndexListView(ListView):
    model = Category
    template_name = 'category/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        cx = super().get_context_data()
        cx['posts'] = Post.objects.filter(category__name=self.kwargs.get('name'))
        return cx
