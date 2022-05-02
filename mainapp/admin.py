from django.contrib import admin

from mainapp.models import ProductCategories, Product

admin.site.register(ProductCategories)
# admin.site.register(Product)

@admin.register(Product)
class Product(admin.ModelAdmin):

    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('price',)
    ordering = ('name', 'price')
    search_fields = ('name',)