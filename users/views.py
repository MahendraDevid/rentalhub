from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from .forms import RegistrationForm
from django.contrib.auth.models import Group
from users.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout  # Import modul logout dari django.contrib.auth

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

class CustomLoginView(LoginView):
    template_name = 'users/login.html'  

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='Pembeli').exists():
                print(f"User '{user.username}' login sebagai pembeli.")
                return reverse('pembeli_dashboard')  # Ganti 'borrower_dashboard' dengan nama URL untuk dashboard peminjam
            elif user.groups.filter(name='Admin').exists():
                print(f"User '{user.username}' login sebagai admin.")
                return reverse('admin_dashboard')  # Ganti 'staff_dashboard' dengan nama URL untuk dashboard petugas
        return super().get_success_url()

@login_required
def admin_dashboard(request):
    is_admin = request.user.groups.filter(name='Admin').exists()
    return render(request, 'dashboard/admin_dashboard.html', {'is_admin': is_admin})

@login_required
def pembeli_dashboard(request):
    return render(request, 'dashboard/pembeli_dashboard.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Set default role to 'Administrator' for newly registered user
            admin_group = Group.objects.get(name='Admin')
            user.groups.add(admin_group)
            return redirect('login')  # Ganti 'login' dengan nama URL untuk halaman login
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def user_list(request):
    if is_admin(request.user):
        users = User.objects.all()
        return render(request, 'users/user_list.html', {'users': users})
    else:
        return HttpResponse("Anda tidak memiliki izin untuk mengakses halaman ini.")
def user_logout(request):
    logout(request)  # Panggil fungsi logout dengan parameter request
    return redirect('login')  # Redirect pengguna ke halaman login setelah logout
