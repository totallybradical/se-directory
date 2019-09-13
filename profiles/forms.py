from django import forms

from .models import Profile
from profile_tags.models import ProfileTag
from django.forms.widgets import CheckboxSelectMultiple

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

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'name', 
            'team',
            'region',
            'tags'
        )
        widgets = {
            'tags': forms.CheckboxSelectMultiple(
                attrs={
                    'class': 'form-check'
                }
            )
        }
    
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields["tags"].widget = CheckboxSelectMultiple()
        self.fields["tags"].queryset = ProfileTag.objects.all()
        for field_name, field in self.fields.items():
            if field_name != "tags":
                field.widget.attrs['class'] = 'form-control form-control-sm'


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     ingredient_id = self.instance.ingredient.id
    #     ingredient = Ingredient.objects.get(id=ingredient_id)
    #     self.fields['quantity'].label = 'Quantity (' + ingredient.quantity_units + ')'
