from django.contrib import admin

from .models import Pinterest

@admin.register(Pinterest)
class PinAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'author')
    list_display_links = ('id', 'name', 'author')
    ordering = ('-released_date',)