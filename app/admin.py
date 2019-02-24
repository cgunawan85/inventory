from django.contrib import admin
from .models import Category, Product, Vendor, Warehouse, InTransaction, OutTransaction


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


class InTransactionAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )
    list_display = ('product', 'quantity', )


class OutTransactionAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )
    list_display = ('product', 'quantity', )


admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(InTransaction, InTransactionAdmin)
admin.site.register(OutTransaction, OutTransactionAdmin)
