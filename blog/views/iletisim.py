import imp
from multiprocessing import context
from django.shortcuts import render



def iletisim(request):
    
    return render(request,'pages/iletisim.html',context={})