from django.contrib import admin
from .models import Tag, Post, Comment

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "slug", "published_at")
    list_filter = ("published_at", "tags")
    search_fields = ("title", "summary", "content")
    autocomplete_fields = ("tags",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("creator", "content_type", "object_id", "created_at")
    list_select_related = ("content_type",)
    search_fields = ("content",)