from django.contrib import admin
from .models import Treasure


@admin.register(Treasure)
class TreasureAdmin(admin.ModelAdmin):
    fields = ['name', 'value', 'material', 'location', 'img_url']
    list_display = ['id', 'name', 'value', 'material', 'location', 'img_url']
    list_filter = ['name', 'value', 'material', 'location', 'img_url']
    search_fields = ['name', 'value', 'material', 'location', 'img_url']

    class Meta:
        model = Treasure
