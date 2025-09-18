from django.contrib import admin
from .models import Category, Size, Prodct, ProductSize, ProductImage
# Register your models here.


class ProductImageInline(admin.TabularInline): # 
    model = ProductImage
    extra = 1  # Number of extra forms to display

class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1

class ProductAdmin(admin.ModelAdmin): # Admin interface for Product model
    list_display = ['name', 'category', 'price', 'color', 'created_at', 'updated_at'] # Поля для отображения в списке
    list_filter = ['category', 'created_at'] # Фильтры в правой части
    search_fields = ['name', 'description', 'color'] # Поля для поиска
    prepopulated_fields = {'slug': ('name',)} # Автоматическое заполнение поля slug на основе name
    inlines = [ProductImageInline, ProductSizeInline]  # Добавляем ProductImageInline в ProductAdmin

class CategoryAdmin(admin.ModelAdmin): # Admin interface for Category model
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Prodct, ProductAdmin)