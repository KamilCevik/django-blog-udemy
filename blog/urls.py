from django.urls import path
from blog.views import iletisim
from blog.views.anasayfa import anasayfa

urlpatterns = [
    path('',anasayfa), 
    path('iletisim', iletisim),
]
