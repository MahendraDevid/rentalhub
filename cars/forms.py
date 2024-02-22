from django import forms
from .models import Mobil

class MobilForm(forms.ModelForm):
    class Meta:
        model = Mobil
        fields = ['Merek', 'Model', 'Tahun', 'Status']
