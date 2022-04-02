from django.shortcuts import get_object_or_404, redirect, render
from blog.models import YazilarModel, yorum
from blog.forms import YorumEkleModelForm, yorum_ekle
from django.views import View
from django.contrib import messages
import logging

logger = logging.getLogger('konu_okuma')


class DetayView(View):
    http_method_names = ['get', 'post']
    yorum_ekleme_formu = YorumEkleModelForm

    def get(self, request, slug):
        yazi = get_object_or_404(YazilarModel, slug=slug)
        if request.user.is_authenticated:    
            logger.info('konu okundu:'+request.user.username)
        yorumlar = yazi.yorumlar.all()
        return render(request,
                      'pages/detay.html',
                      context={
                          'yazi': yazi,
                          'yorumlar': yorumlar,
                          'yorum_ekle_form': self.yorum_ekleme_formu
                      })

    def post(self, request, slug):
        yazi = get_object_or_404(YazilarModel, slug=slug)
        yorum_ekleme_formu = self.yorum_ekleme_formu(request.POST)
        if yorum_ekleme_formu.is_valid():
            yorum = yorum_ekleme_formu.save(commit=False)
            yorum.yazan = request.user
            yorum.yazi = yazi
            yorum.save()
            messages.success(request, 'Yorum Başarıyla Eklendi.')
        return redirect('detay', slug=slug)
