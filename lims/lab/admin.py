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
    list_display = ['__str__', 'get_contract', 'get_invoices']

    def get_invoices(self, obj):
        return mark_safe('; '.join([
            f'<a href="{reverse("admin:lab_invoice_change", args=(item.pk,))}">{item.__str__()}</a>'
            for item in obj.invoices.all()
        ]))

    def get_contract(self, obj):
        return mark_safe(
            f'<a href="{reverse("admin:lab_contract_change", args=(obj.contract.pk,))}">{obj.contract.__str__()}</a>'
        )

    get_invoices.short_description = 'Счета'
    get_contract.short_description = 'Договоры'


class ContractAdmin(admin.ModelAdmin):
    inlines = [BidInline]
    list_display = ['__str__', 'get_bids', 'get_invoices']

    def get_bids(self, obj):
        return mark_safe('; '.join([
            f'<a href="{reverse("admin:lab_bid_change", args=(item.pk,))}">{item.__str__()}</a>'
            for item in obj.bids.all()
        ]))

    def get_invoices(self, obj):
        return mark_safe('; '.join([
            f'<a href="{reverse("admin:lab_invoice_change", args=(item.pk,))}">{item.__str__()}</a>'
            for item in self.list_all_invoices(obj)
        ]))

    def list_all_invoices(self, obj):
        invoices = []
        for bid in obj.bids.all():
            for invoice in bid.invoices.all():
                invoices.append(invoice)
        return invoices

    get_invoices.short_description = 'Счета'
    get_bids.short_description = 'Заявки'


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'get_bids', 'get_contract']

    def get_bids(self, obj):
        return mark_safe('; '.join([
            f'<a href="{reverse("admin:lab_bid_change", args=(item.pk,))}">{item.__str__()}</a>'
            for item in obj.bids.all()
        ]))

    def get_contract(self, obj):
        return mark_safe('; '.join([
            f'<a href="{reverse("admin:lab_contract_change", args=(item.contract.pk,))}">{item.contract.__str__()}</a>'
            for item in obj.bids.all()
        ]))

    get_bids.short_description = 'Заявки'
    get_contract.short_description = 'Договоры'


admin.site.register(Methodic, MethodicAdmin)
admin.site.register(Reagent, ReagentAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(TechnicalMaintenance, TechnicalMaintenanceAdmin)
admin.site.register(Protocol)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Invoice, InvoiceAdmin)
