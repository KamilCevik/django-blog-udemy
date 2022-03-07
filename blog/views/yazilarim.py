from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required(login_url='anasayfa')
def yazilarim(request):
     
    
    yazilar=request.user.yazilar.order_by('-id')
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar, 2)

    return render(request,'pages/yazilarim.html',context={
        'yazilar': paginator.get_page(sayfa),
    })
