from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'text', 'created_time']
    # 把新增的 PostAdmin 也注册进来
    admin.site.register(Comment)
