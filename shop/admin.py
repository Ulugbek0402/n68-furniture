
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','price','is_active','created_at')
    list_filter = ('category','is_active')
    search_fields = ('title','description')
    prepopulated_fields = {'slug': ('title',)}
