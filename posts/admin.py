from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import post


class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(post, PostAdmin)
