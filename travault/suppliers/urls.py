from django.urls import path
from . import views

urlpatterns = [
    path('', views.supplier_list, name='supplier_list'),
    path('<int:supplier_id>/', views.supplier_detail, name='supplier_detail'),
    path('create/', views.supplier_create, name='supplier_create'),
    path('<int:supplier_id>/update/', views.supplier_update, name='supplier_update'),
    path('<int:supplier_id>/delete/', views.supplier_delete, name='supplier_delete'),
]