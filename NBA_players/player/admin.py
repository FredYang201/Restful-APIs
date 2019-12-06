from django.contrib import admin
from .models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'link', 'position', 'height', 'weight', 'born', 'age', 'years_in_nba', 'team']
    list_filter = ['number', 'position', 'age', 'years_in_nba', 'team']


admin.site.register(Player, PlayerAdmin)