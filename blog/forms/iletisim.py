from dataclasses import field
from django import forms

from blog.models.iletisim import IletisimModel

class IletisimForm(forms.ModelForm):
    class Meta:
        model=IletisimModel
        fields=('isim_soyisim','email','mesaj')
        
   