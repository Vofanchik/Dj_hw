from django.contrib import admin

from .models import Stock, StockProduct, Product

class ProductStockInline(admin.TabularInline):
    model = StockProduct
    # formset = ArticleScopesInlineFormset

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = [ProductStockInline]

@admin.register(Product)
class StockAdmin(admin.ModelAdmin):
    model = Product
