from django.contrib import admin
from .models import Aprest


class AprestAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)

admin.site.register(Aprest, AprestAdmin)