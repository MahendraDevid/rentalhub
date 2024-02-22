from django.urls import path
from . import views

urlpatterns = [
    path('', views.mobil_list, name='mobil_list'),
    path('create/', views.mobil_create, name='mobil_create'),  # Tambahkan ini untuk pola URL membuat mobil
    path('<str:mobil_id>/', views.mobil_detail, name='mobil_detail'),
    path('<str:mobil_id>/update/', views.mobil_update, name='mobil_update'),
    path('<str:mobil_id>/delete/', views.mobil_delete, name='mobil_delete'),
]
