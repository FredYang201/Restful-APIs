from django.contrib import admin
from .models import Country


class CountryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'capital',
        'population',
        'area',
        'continent',
        'flag',
        'phone',
        'currency',
        'created']
    list_filter = ('continent', )


admin.site.register(Country, CountryAdmin)
