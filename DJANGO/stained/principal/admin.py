from django.contrib import admin, messages
from .models import Profile
import datetime

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'code')
    readonly_fields=('created', 'updated')
    search_fields = ('user', 'code')


    admin.site.site_header = 'Stained Glass'
    admin.site.index_title = 'Panel de control Stained Glass'
    admin.site.site_title = 'Stained Admin'


    def actualizar(modeladmin, request, queryset):

        queryset.update(f_inicio=datetime.datetime.now())
        queryset.update(f_fin=datetime.datetime.now()+datetime.timedelta(days=30))
        queryset.update(active=True)
        messages.success(request, "Actualizado")

    admin.site.add_action(actualizar, "Actualizar")



admin.site.register(Profile, ProfileAdmin)