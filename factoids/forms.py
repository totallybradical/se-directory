from django import forms

from .models import Factoid

class FactoidForm(forms.ModelForm):

    class Meta:
        model = Factoid
        fields = ('text', 'is_fun')