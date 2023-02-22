import datetime

from django import forms

from .models import Methodic, Reagent, Equipment, Protocol, TechnicalMaintenance, Bid, Invoice, Contract


class MethodicCreateForm(forms.ModelForm):
    class Meta:
        model = Methodic
        fields = '__all__'
        widgets = {
            'acts_from': forms.SelectDateWidget(
                years=range(datetime.date.today().year - 50, datetime.date.today().year + 30)
            ),
            'acts_to': forms.SelectDateWidget(
                years=range(datetime.date.today().year - 30, datetime.date.today().year + 30)
            ),
        }

    used_reagents = forms.ModelMultipleChoiceField(
        queryset=Reagent.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    used_equipment = forms.ModelMultipleChoiceField(
        queryset=Equipment.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class ProtocolCreateForm(forms.ModelForm):
    class Meta:
        model = Protocol
        fields = '__all__'


class ReagentCreateForm(forms.ModelForm):
    class Meta:
        model = Reagent
        fields = '__all__'


class EquipmentCreateForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'


class ContractCreateForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'


class BidCreateForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = '__all__'


class InvoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'


class MaintenanceCreateForm(forms.ModelForm):
    equipment = forms.ModelMultipleChoiceField(
        queryset=Equipment.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = TechnicalMaintenance
        fields = '__all__'
        widgets = {
            'next_date': forms.SelectDateWidget(
            ),
        }
        labels = {
            'equipment': 'Относится к оборудованию'
        }

