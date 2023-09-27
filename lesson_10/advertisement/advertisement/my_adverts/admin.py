from django.contrib import admin
from .models import Advertisement
# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author', 'price', 'created_date', 'updated_date', 'auction', 'category', 'image', 'image_img']
    list_filter = ['auction', 'author', 'created_at', 'updated_at']
    actions=['forbid_the_auction', 'permit_the_auction']
    readonly_fields = ['image_img']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'category', 'user', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        }),
    )




    @admin.action(description="Убрать возможность торга")
    def forbid_the_auction(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга")
    def permit_the_auction(self, request, queryset):
        queryset.update(auction=True)




admin.site.register(Advertisement, AdvertisementAdmin)