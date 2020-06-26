from django.contrib import admin
from .models import ReceivedItem, IssuedItem, BalanceItemQuantity

class ItemBalance(admin.ModelAdmin):
    list_display = ('item', 'get_stock')
    class Meta:
        model = BalanceItemQuantity

class ReceivedAdmin(admin.ModelAdmin):
    list_display = ('item', 'total_received')
    class Meta:
        model = ReceivedItem

class IssuedAdmin(admin.ModelAdmin):
    list_display = ('item', 'total_issued')
    class Meta:
        model = IssuedItem
        

admin.site.register(ReceivedItem, ReceivedAdmin)
admin.site.register(IssuedItem, IssuedAdmin)
admin.site.register(BalanceItemQuantity, ItemBalance)