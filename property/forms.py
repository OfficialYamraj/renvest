from django import forms
from .models import MapLocater


class MeasurementModelForm(forms.ModelForm):
    class Meta:
        model = MapLocater
        fields = ('destination',)
