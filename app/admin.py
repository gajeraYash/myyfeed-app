from django.contrib import admin
from app.models import *
# Register your models here.

class ChatMessage(admin.TabularInline):
    model = ChatMessage

class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessage]
    class Meta:
        model = Thread 
admin.site.register(UserProfile)
admin.site.register(UserAnnoucement)
admin.site.register(Follower)
admin.site.register(UserComment)
admin.site.register(Thread, ThreadAdmin)