import django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import ProfiDuzenlemeForm


@login_required(login_url='/')
def profil_guncelle(request):
    if request.method == 'POST':
        form = ProfiDuzenlemeForm(request.POST,
                                  request.FILES,
                                  instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil Güncellendi')
    else:
        form = ProfiDuzenlemeForm(instance=request.user)

    return render(request,
                  'pages/profil-guncelle.html',
                  context={'form': form})
