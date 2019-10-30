from django import forms

from .models import Factoid

class FactoidForm(forms.ModelForm):

    class Meta:
        model = Factoid
        fields = ('text', 'is_fun')

    def __init__(self, *args, **kwargs):
        super(FactoidForm, self).__init__(*args, **kwargs)
        self.fields['is_fun'].label = "Fun Fact?"
        self.fields['text'].label = ""
        for field_name, field in self.fields.items():
            if field_name == 'text':
                field.widget.attrs['class'] = 'form-control form-control-sm'