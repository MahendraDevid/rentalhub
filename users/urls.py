from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # Path untuk login dan register
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),  # URL untuk view logout
    
    # Path untuk dashboard
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('pembeli-dashboard/', views.pembeli_dashboard, name='pembeli_dashboard'),
    
    # path untuk user
    path('list/', views.user_list, name='user_list'),
]
