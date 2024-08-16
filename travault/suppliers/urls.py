from django.urls import path
from . import views

urlpatterns = [
    path('', views.supplier_list, name='supplier_list'),
    path('add/', views.supplier_add, name='supplier_add'),
    path('edit/', views.supplier_edit, name='supplier_edit'),
    path('process/', views.supplier_process, name='supplier_process'),
    path('process/add/', views.supplier_process_add, name='supplier_process_add'),
    path('process/edit/', views.supplier_process_edit, name='supplier_process_edit'),
]