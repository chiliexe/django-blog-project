from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at', 'published')
    list_display_links = ('title',)
    list_editable = ('published',)
    search_fields = ('title',)


admin.site.register(Post, PostAdmin)
