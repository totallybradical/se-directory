from django import forms

from .models import Profile
from profile_tags.models import ProfileTag
from django.forms.widgets import CheckboxSelectMultiple
from django.utils.safestring import mark_safe


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'name',
            'profile_pic',
            'geo',
            'team',
            'region',
            'primary_strength',
            'secondary_strength',
            'tags'
        )


def thumbnail(image_path, width, height):
    absolute_url = '/' + image_path
    return '<img src="%s" alt="%s" width="%s" height="%s" class="widget-img" />' % (absolute_url, image_path, width, height)


class ImageWidget(forms.FileInput):
    template = '<div class="container"><center>%(image)s</center></div>' \
               '<br>' \
               '<div class="custom-file">%(input)s<label class="custom-file-label" for="customFile">Choose image file...</label></div>'

    def __init__(self, attrs=None, template=None, width=189, height=252):
        if template is not None:
            self.template = template
        self.width = width
        self.height = height
        super(ImageWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        attrs = {
            'id': 'customFile'
        }
        input_html = super(forms.FileInput, self).render(name, value, attrs, renderer=None)
        if value and hasattr(value, 'width') and hasattr(value, 'height'):
            image_html = thumbnail(value.name, self.width, self.height)
            output = self.template % {'input': input_html,
                                      'image': image_html
            }
        else:
            output = input_html
        return mark_safe(output)


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'name',
            'profile_pic',
            'geo',
            'team',
            'region',
            'primary_strength',
            'secondary_strength',
            'tags'
        )
        widgets = {
            'profile_pic': ImageWidget,
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
