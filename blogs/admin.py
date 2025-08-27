from django.contrib import admin
from .models import BlogCategoryModel, TagModel, ComentModel, BlogModel


@admin.register(BlogCategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("-created_at",)


@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(ComentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "blog", "email", "created_at")
    search_fields = ("email", "text")
    list_filter = ("created_at",)


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "created_at")
    search_fields = ("title", "short_description", "long_description")
    list_filter = ("category", "tags", "created_at")
    filter_horizontal = ("tags",)  
