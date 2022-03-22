from dataclasses import fields
from pyexpat import model
from django import forms
from blog.models import YorumModel
class YorumEkleModelForm(forms.ModelForm):
    class Meta:
        model=YorumModel
        fields=('yorum',)