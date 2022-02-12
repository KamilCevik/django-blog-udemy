from multiprocessing import context
from django.shortcuts import render

def anasayfa(request):
    context={
        'isim':'Kamil ÇEVİK'
    }
    return render(request,'pages/anasayfa.html',context=context)