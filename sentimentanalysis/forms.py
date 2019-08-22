from django import forms
from django.core.exceptions import ValidationError

class IsValidForm(forms.Form):
    url = forms.URLField()
    url2 = forms.URLField(required=False)

    def clean(self):
        if self.cleaned_data['url']:
            raise ValidationError('Please enter valid URL', code='invalid')
