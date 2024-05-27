from django.contrib import admin
from .models import *
from django.utils.html import format_html

class ChatMessageInline(admin.TabularInline):
    model = ChatMessage


class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessageInline]




admin.site.register(Post)
admin.site.register(User_info)

admin.site.register(ChatMessage)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(customer_details)
