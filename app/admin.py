from django.contrib import admin
from .models import Category, Product, Vendor, Warehouse


class WarehouseAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )
    list_display = ('name', 'created_at', )


class VendorAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )
    list_display = ('name', 'created_at', )


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )
    list_display = ('name', 'created_at', )


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )
    list_display = ('brand', 'name', 'category', 'warehouse', 'stock', 'location', )


admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
