from django.contrib import admin
from blog.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    ordering = ['created_date']
    list_filter = ['status']
admin.site.register(Post,PostAdmin)