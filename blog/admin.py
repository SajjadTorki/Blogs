from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=("title","date_time_modified","date_time_changed","status")

admin.site.register(Post,PostAdmin)