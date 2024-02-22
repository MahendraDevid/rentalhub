from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Mobil
from .forms import MobilForm
from .utils import is_admin

@login_required
def mobil_list(request):
    if is_admin(request.user):
        mobil = Mobil.objects.all()
    else:
        mobil = Mobil.objects.filter(Status='Tersedia')  # Hanya tampilkan mobil yang tersedia untuk pembeli
    return render(request, 'cars/mobil_list.html', {'mobil': mobil})

@login_required
def mobil_detail(request, mobil_id):
    mobil = get_object_or_404(Mobil, MobilID=mobil_id)
    return render(request, 'cars/mobil_detail.html', {'mobil': mobil})

@user_passes_test(lambda u: u.groups.filter(name='Admin').exists())
@login_required
def mobil_create(request):
    if not is_admin(request.user):
        return HttpResponseForbidden("Anda tidak memiliki izin untuk melakukan operasi ini.")
    
    if request.method == 'POST':
        form = MobilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mobil_list')
    else:
        form = MobilForm()
    return render(request, 'cars/mobil_form.html', {'form': form})

@login_required
def mobil_update(request, mobil_id):
    if not is_admin(request.user):
        return HttpResponseForbidden("Anda tidak memiliki izin untuk melakukan operasi ini.")
    
    mobil = get_object_or_404(Mobil, MobilID=mobil_id)
    if request.method == 'POST':
        form = MobilForm(request.POST, instance=mobil)
        if form.is_valid():
            form.save()
            return redirect('mobil_list')
    else:
        form = MobilForm(instance=mobil)
    return render(request, 'cars/mobil_form.html', {'form': form})

@login_required
def mobil_delete(request, mobil_id):
    if not is_admin(request.user):
        return HttpResponseForbidden("Anda tidak memiliki izin untuk melakukan operasi ini.")
    
    mobil = get_object_or_404(Mobil, MobilID=mobil_id)
    mobil.delete()
    return redirect('mobil_list')
