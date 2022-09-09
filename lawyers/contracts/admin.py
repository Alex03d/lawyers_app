from django.contrib import admin

from .models import Contract, Attorney, Client

admin.site.register(Contract)
admin.site.register(Attorney)
admin.site.register(Client)


class ContractAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'client',
        'date',
        'description',
    )
    list_editable = ('description',)
    search_fields = ('attorney',)
    list_filter = ('date',)
    empty_value_display = '-пусто-'

class AttorneyAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'full_name',
    )
    empty_value_display = '-пусто-'

class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'full_name',
    )
    empty_value_display = '-пусто-'

