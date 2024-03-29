from re import template
from urllib import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from blog.models import YazilarModel
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class YaziSilDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('giris')
    template_name = 'pages/yazi_sil_onay.html'
    success_url = reverse_lazy('yazilarim')

    def get_queryset(self):
        yazi = YazilarModel.objects.filter(slug=self.kwargs['slug'],
                                           yazar=self.request.user)
        return yazi
