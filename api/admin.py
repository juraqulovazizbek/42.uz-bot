from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'telegram_username')
    search_fields = ('chat_id', 'telegram_username')
    list_filter = ('telegram_username',)
    