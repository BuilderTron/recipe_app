from django.contrib import admin
from .models import Recipe, Category, Meal



# admin.site.register(Profile)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)




class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Meal, MealAdmin)




class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Recipe, RecipeAdmin)
