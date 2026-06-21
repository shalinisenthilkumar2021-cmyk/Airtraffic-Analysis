from django import forms

class UploadForm(forms.Form):
    file = forms.FileField()

from django import forms
from .models import FlightData

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = FlightData
        fields = ['file']