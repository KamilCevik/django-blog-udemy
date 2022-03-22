from unicodedata import name
from django.urls import path, include
from blog.views import iletisim, anasayfa, kategori, yazilarim, yazi_ekle
from blog.views.detay import detay
from blog.views.yazi_guncelle import yazi_guncelle
from blog.views.yazi_sil import yazi_sil

urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('iletisim', iletisim, name='iletisim'),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', detay, name='detay'),
    path('yazi-ekle', yazi_ekle, name='yazi-ekle'),
    path('yazi-guncelle/<slug:slug>', yazi_guncelle, name='yazi-guncelle'),
    path('yazi-sil/<slug:slug>', yazi_sil, name='yazi-sil'),
    
]
