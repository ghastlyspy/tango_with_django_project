from django.contrib import admin
from rango.models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'views', 'likes']
    prepopulated_fields = {'slug': ('name',)}


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url']
    list_filter = ['category']
    list_editable = ['category']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
