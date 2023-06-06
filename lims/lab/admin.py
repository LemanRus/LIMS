# Copyright 2023 Firsov Vlad aka LemanRus
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Methodic, Reagent, Equipment, TechnicalMaintenance, Protocol, Contract, Bid, Invoice, Record


class ReagentInline(admin.TabularInline):
    model = Methodic.used_reagents.through
    extra = 0


class ReagentAdmin(admin.ModelAdmin):
    inlines = [ReagentInline]


class MethodicAdmin(admin.ModelAdmin):
    inlines = [ReagentInline]
    exclude = ['used_reagents']


class TechnicalMaintenanceInline(admin.TabularInline):
    model = TechnicalMaintenance
    extra = 0


# class TechnicalMaintenanceAdmin(admin.ModelAdmin):
#     def get_model_perms(self, request):
#         return {}


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


class ProtocolAdmin(admin.ModelAdmin):
    pass


class RecordAdmin(admin.ModelAdmin):
    pass



admin.site.register(Methodic, MethodicAdmin)
admin.site.register(Reagent, ReagentAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(TechnicalMaintenance)
admin.site.register(Protocol, ProtocolAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Record, RecordAdmin)
