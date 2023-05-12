import datetime

from django import forms

from .models import Methodic, Reagent, Equipment, Protocol, TechnicalMaintenance, Bid, Invoice, Contract, Record


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
        widgets = {
            'close_date': forms.SelectDateWidget(
                years=range(datetime.date.today().year - 5, datetime.date.today().year + 1)
            )
        }


class ReagentCreateForm(forms.ModelForm):
    class Meta:
        model = Reagent
        fields = '__all__'
        widgets = {
            'made_date': forms.SelectDateWidget(
                years=range(datetime.date.today().year - 50, datetime.date.today().year + 1)
            ),
            'best_before': forms.SelectDateWidget(
                years=range(datetime.date.today().year - 30, datetime.date.today().year + 50)
            ),
        }


class EquipmentCreateForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'
        widgets = {
            'last_cal': forms.SelectDateWidget(
                years=range(datetime.date.today().year - 15, datetime.date.today().year + 1)
            ),
            'next_cal': forms.SelectDateWidget(
                years=range(datetime.date.today().year, datetime.date.today().year + 15)
            ),
        }


class ContractCreateForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
        widgets = {
            'date_conclusion': forms.SelectDateWidget(
                years=range(datetime.date.today().year - 15, datetime.date.today().year + 16)
            ),
            'date_end': forms.SelectDateWidget(
                years=range(datetime.date.today().year - 15, datetime.date.today().year + 16)
            ),
        }


class BidCreateForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = '__all__'
        widgets = {
            'invoices': forms.CheckboxSelectMultiple,
        }


class InvoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'


class MaintenanceCreateForm(forms.ModelForm):
    class Meta:
        model = TechnicalMaintenance
        fields = '__all__'
        widgets = {
            'next_date': forms.SelectDateWidget(),
        }


class RecordCreateForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['text', 'file']
