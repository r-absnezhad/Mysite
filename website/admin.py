from django.contrib import admin
from website.models import Contact,Newsletter
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    ordering = ['created_date']
    list_display = ('name', 'email', 'created_date')
    list_filter = ('email', )
admin.site.register(Contact,ContactAdmin)

class NewsletterAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    ordering = ['created_date']
    list_display = ('email', 'created_date')
    list_filter = ('email', )
admin.site.register(Newsletter,NewsletterAdmin)