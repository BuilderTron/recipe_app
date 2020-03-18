from django.contrib import admin
from .models import Recipe, Category



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)



class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Recipe, RecipeAdmin)
