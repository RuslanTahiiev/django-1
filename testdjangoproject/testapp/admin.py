from django.contrib import admin

from .models import ChatMessage


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_date',)
    list_display_links = ('name',)
    search_fields = ('create_date',)
    list_editable = ('create_date',)
    list_filter = ('name', 'create_date',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ChatMessage, MessageAdmin)
