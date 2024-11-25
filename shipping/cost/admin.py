from django.contrib import admin
from .models import ShippingCost
# Register your models here.
admin.site.register(ShippingCost)
# @admin.register(ShippingCost)
# class ShippingCostAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'PriceField' : ('unit',)}
