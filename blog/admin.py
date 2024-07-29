from django.contrib import admin
from blog.models import Post,Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    ordering = ['created_date']
    list_filter = ['status']
    summernote_fields = ('content',)

admin.site.register(Post,PostAdmin)
admin.site.register(Category)