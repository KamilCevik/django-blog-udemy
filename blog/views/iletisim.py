import imp
from multiprocessing import context
from django.shortcuts import render, redirect
from blog.forms import IletisimForm
from blog.models import IletisimModel
from django.views.generic import FormView


class İletisimFormView(FormView):
    template_name = 'pages/iletisim.html'
    form_class = IletisimForm
    success_url = 'email-gonderildi'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)