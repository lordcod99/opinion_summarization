from dataclasses import fields
import imp
from django import forms
from .models import data


class inputForm(forms.ModelForm):
    class Meta:
        model = data
        fields = [
            'input_data',
        ]