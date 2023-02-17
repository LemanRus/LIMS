import datetime

from django import forms

from .models import Methodic, Reagent, Equipment


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
