from django.contrib import admin
from .models import Product , Order , Cart

# Register your models here.


class ModelAdminProduct(admin.ModelAdmin):
    list_display=['name','price','description','image']
    # list_filter=['name','author']
    # search_fields=['name','author']
    # list_editable=['price']

    actions=['mark_free']
    def mark_free(self,request,queryset):
        queryset.update(price=0)
        self.message_user(request,'items marked as free')
    mark_free.short_description='Mark selected items as free'                                                                                                                                                       



admin.site.register(Product,ModelAdminProduct) 
