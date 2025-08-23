from django.contrib import admin

from .models import CategoryModel, CatalogModel, ProductModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(CatalogModel)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'catalog', 'price', 'created_at', 'updated_at')
    search_fields = ('name', 'short_description')
    list_filter = ('category', 'catalog', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    list_editable = ('price',)
