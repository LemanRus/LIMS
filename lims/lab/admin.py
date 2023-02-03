from django.contrib import admin
from .models import Methodic, Reagent


class ReagentInline(admin.TabularInline):
    model = Methodic.used_reagents.through
    extra = 0


class ReagentAdmin(admin.ModelAdmin):
    inlines = [ReagentInline]


class MethodicAdmin(admin.ModelAdmin):
    inlines = [ReagentInline]
    exclude = ['used_reagents']


admin.site.register(Methodic, MethodicAdmin)
admin.site.register(Reagent, ReagentAdmin)