from django.contrib import admin
from .models import Product,Category
# Register your models here.
admin.site.register(Category)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','condition','seller','is_approved')
    list_filter=('is_approved','condition','category')
    search_fields=('name','seller__username')
    actions=['approve_products']
    def approve_products(self,request,queryset):
        queryset.update(is_approved=True)