from django.contrib import admin
from .models import Item, ItemImage, Category

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'item_id')
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ( 'title',)
    # list_filter = ('item_id',)
    class Meta:
        model = Item

class ItemImageAdmin(admin.ModelAdmin):
    list_display = ('item', 'featured',)
    class Meta:
        model = ItemImage

class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug': ('catname', )}
    
    class Meta:
        model = Category
        
    
        
admin.site.site_header = 'LTWP online store management'
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage, ItemImageAdmin)
admin.site.register(Category, CatAdmin)