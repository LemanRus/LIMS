from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Methodic, Reagent, Equipment, TechnicalMaintenance, Protocol, Contract, Bid, Invoice


class ReagentInline(admin.TabularInline):
    model = Methodic.used_reagents.through
    extra = 0


class ReagentAdmin(admin.ModelAdmin):
    inlines = [ReagentInline]


class MethodicAdmin(admin.ModelAdmin):
    inlines = [ReagentInline]
    exclude = ['used_reagents']


class TechnicalMaintenanceInline(admin.TabularInline):
    model = Equipment.maintenance.through
    extra = 0


class TechnicalMaintenanceAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class EquipmentAdmin(admin.ModelAdmin):
    inlines = [TechnicalMaintenanceInline]
    exclude = ['maintenance']


class BidInline(admin.TabularInline):
    show_change_link = True
    model = Bid
    extra = 0


class InvoicesInline(admin.TabularInline):
    show_change_link = True
    model = Bid.invoices.through
    extra = 0


class BidAdmin(admin.ModelAdmin):
    inlines = [InvoicesInline]
    exclude = ['invoices']
    list_display = ['number', 'contract', 'get_invoices']

    def get_invoices(self, obj):
        return "; ".join([invoice.__str__() for invoice in obj.invoices.all()])


class ContractAdmin(admin.ModelAdmin):
    inlines = [BidInline]
    list_display = ['__str__', 'get_bids']

    def get_bids(self, obj):
        return mark_safe('; '.join([i for i in self.bids_links(obj)]))

    def bids_links(self, obj):
        links = [f'<a href="{reverse("admin:lab_bid_change", args=(item.pk,))}">{item.__str__()}</a>' for item in obj.bids.all()]
        return links

    bids_links.short_description = 'bid'


admin.site.register(Methodic, MethodicAdmin)
admin.site.register(Reagent, ReagentAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(TechnicalMaintenance, TechnicalMaintenanceAdmin)
admin.site.register(Protocol)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Invoice)
