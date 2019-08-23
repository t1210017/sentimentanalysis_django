from django import forms
from django.core.exceptions import ValidationError
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

class IsValidForm(forms.Form):
    url = forms.URLField()
    url2 = forms.URLField(required=False)

    try:
         html = urlopen(url)
    except HTTPError as e:
         raise ValidationError('存在しないURLです', code='invalid')
    try:
         html = urlopen(url2)
    except HTTPError as e:
         raise ValidationError('存在しないURLです', code='invalid')
    def clean(self):
        if self.cleaned_data['url']:
            raise ValidationError('URLの形式が正しくありません', code='invalid')
