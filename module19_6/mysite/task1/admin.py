from django.contrib import admin
from .models import Buyer, Game, News


admin.site.register(News)


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age', )  # фильтрация
    list_display = ('name', 'balance', 'age', ) #поле для отображения в списке
    search_fields = ('name', ) #поле для поиска
    list_per_page = 30#кол-во на странице
    readonly_fields = ('balance', )# только для чтения


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost', )
    list_display = ('title', 'cost', 'size', )
    search_fields = ('title',)
    list_per_page = 20

# Register your models here.
