from dataclasses import field
from django import forms
from django.core.mail import send_mail

from blog.models.iletisim import IletisimModel

class IletisimForm(forms.ModelForm):
    class Meta:
        model=IletisimModel
        fields=('isim_soyisim','email','mesaj')
    
    def send_mail(self,mesaj):
        send_mail(
            subject='İletişim Formundan Yeni Mesaj Var',
            message=mesaj,
            from_email='valoo3236@gmail.com',
            recipient_list=['valoo3236@gmail.com'],
            fail_silently=False
        )
   