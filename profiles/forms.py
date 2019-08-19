from django import forms

from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'name',
            'team',
            'region',
            'primary_strength',
            'secondary_strength'
        )